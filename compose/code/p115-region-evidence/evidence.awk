# evidence.awk -- STAGE A. Classify a `git ls-tree -r` stream into the files
# that can carry a DECLARED affiliation, and nothing else.
#
# Input : git ls-tree -r <ref>     (<mode> SP <type> SP <sha> TAB <path>)
# Output: one record per evidence blob, plus counters
#
#   S <kind> <sha> <depth> <path>     a structured metadata file
#   R readme  <sha> <depth> <path>    the root README (layer R)
#   C <key> <value>                   counters
#
# P115-B. LAYER S IS A CLOSED LIST OF FILENAMES, MATCHED ON THE BASENAME.
# `docs/requirements.rst` taught this KB (P112-A) that substring matching on
# paths invents members; the same rule applies here. `my-package.json` is not
# `package.json` and is not read.
#
# P115-F. A VENDORED TREE IS SOMEBODY ELSE'S DECLARATION.
# `node_modules/left-pad/package.json` carries left-pad's author, not this
# repository's, and on a shelf where 5 rows vendor their dependencies
# (P114-D) reading it would place those rows wherever their largest
# dependency happens to live. Vendored prefixes are excluded here, before
# any body is fetched, and the exclusion is COUNTED so the drop is visible.
#
# CAP. At most `cap` structured blobs are emitted per repository, longest
# path last (shallowest first, so the root manifest is never the one dropped).
# P1040: a capped row is DECLARED (`C capped 1`), never silently short.

BEGIN { FS = "\t"; cap = (cap == "" ? 40 : cap + 0) }

{
  path = $2
  if (path == "") next
  sha = $1
  sub(/^[0-7]+ [a-z]+ /, "", sha)
  sub(/ .*$/, "", sha)
  nfiles++

  # ---- vendored? ---------------------------------------------------------
  if (path ~ /(^|\/)(node_modules|vendor|third_party|thirdparty|bower_components|\.venv|venv|site-packages|Pods|\.git|\.tox|\.mypy_cache|__pycache__)\//) {
    nvendored++
    next
  }

  n = split(path, seg, "/")
  base = seg[n]
  depth = n - 1

  kind = ""
  if (base == "CITATION.cff" || base == "CITATION.CFF")      kind = "cff"
  else if (base == "codemeta.json")                          kind = "codemeta"
  else if (base == ".zenodo.json")                           kind = "zenodo"
  else if (base == "package.json")                           kind = "npm"
  else if (base == "composer.json")                          kind = "composer"
  else if (base == "pyproject.toml")                         kind = "pytoml"
  else if (base == "setup.cfg")                              kind = "setupcfg"
  else if (base == "setup.py")                               kind = "setuppy"
  else if (base == "pom.xml")                                kind = "maven"
  else if (base == "Cargo.toml")                             kind = "cargo"
  else if (base == "go.mod")                                 kind = "gomod"
  else if (base == "pubspec.yaml")                           kind = "pubspec"
  else if (base == "DESCRIPTION" && depth == 0)              kind = "rdesc"
  else if (base ~ /\.gemspec$/)                              kind = "gemspec"

  if (kind != "") {
    nS++
    if (depth == 0) nS0++
    kinds[kind] = 1
    # keyed by depth so the sort below is stable and shallow-first
    rec[++nrec] = kind "\t" sha "\t" depth "\t" path
    recdepth[nrec] = depth
    next
  }

  # ---- layer R: the ROOT readme only ------------------------------------
  if (depth == 0 && toupper(base) ~ /^README(\.|$)/) {
    nR++
    readme = "readme\t" sha "\t0\t" path
  }
}

END {
  # shallow-first, so a cap can only ever drop the deepest declarations
  for (d = 0; d <= 64 && emitted < cap; d++)
    for (i = 1; i <= nrec && emitted < cap; i++)
      if (recdepth[i] == d) { print "S\t" rec[i]; emitted++ }

  if (readme != "") print "R\t" readme

  nkinds = 0
  for (k in kinds) nkinds++

  print "C\tfiles\t"      nfiles + 0
  print "C\tvendored\t"   nvendored + 0
  print "C\tstruct\t"     nS + 0
  print "C\troot_struct\t" nS0 + 0
  print "C\tstruct_read\t" emitted + 0
  print "C\tkinds\t"      nkinds + 0
  print "C\treadme\t"     nR + 0
  print "C\tcapped\t"     ((nS + 0) > emitted ? 1 : 0)
}
