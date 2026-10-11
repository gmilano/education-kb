# place.awk -- STAGE C. Turn address tokens into a REGION, or into a stated
# reason why no region can be read.
#
# Usage: awk -f place.awk country.region.tsv stoplist.tsv tokens
# Output: key=value lines, one per line, for `eval` by the driver.
#
# ---------------------------------------------------------------------------
# P115-J. THE REGION COLUMN OF `country.region.tsv` IS THE COUNTRY'S REGION.
# THE CLASS COLUMN DECIDES WHETHER A HOSTNAME MAY USE IT. The two are not the
# same question: `.be` IS Belgium and Belgium IS in EMEA, and `youtu.be` is
# still not evidence of anything. So a HOSTNAME places only on class `cc`,
# while a TYPED country field (CITATION.cff `country:`, ISO-3166 alpha-2 by
# its own schema) places on `cc` or `vanity` -- a typed field is a
# declaration, not an address, and the vanity trap does not apply to it.
# Class `cc?` never places through either door.
#
# P115-K. TWO REGIONS IN THE EVIDENCE IS `contested`, NEVER A MAJORITY VOTE.
# A repository whose metadata carries a `.fi` maintainer and a `.jp`
# maintainer is a genuinely cross-regional project, and the brief's `region`
# is a single closed value. Counting whichever appears more often would turn
# a real collaboration into a confident single answer. It is left UNPLACED
# and counted as contested, which is a result a reader can act on.

BEGIN { FS = "\t" }

# ---- the three inputs, taken BY POSITION, never by filename -------------
#
# P115-M. THIS INSTRUMENT IDENTIFIES ITS INPUTS BY ARGUMENT POSITION BECAUSE
# ITS FIRST CENSUS RUN IDENTIFIED THEM BY FILENAME AND READ NEITHER.
# The driver materialises the two committed maps into its work directory --
# it has to, because `P115_NO_STOP` and `P115_NO_VANITY` are REWRITES of them
# -- and the copies are not named `country.region.tsv` and `stoplist.tsv`.
# A `FILENAME ~ /country\.region\.tsv$/` rule therefore matched nothing, both
# maps fell through to the token rules, every TLD read as unknown, and six
# real repositories came back `no-country` with a straight face. The figures
# were wrong and NOTHING in the output said so.
#
# So: position, plus the `MAPFAIL` guard in END. A census that silently reads
# an empty map produces 296 confident zeros, and zeros are the one result
# nobody re-checks.
FNR == 1 { nfile++ }

nfile == 1 {
  if ($0 ~ /^#/ || NF < 3) next
  cls[$1] = $2
  reg[$1] = $3
  if ($2 == "cc") nmap++
  next
}

nfile == 2 {
  if ($0 ~ /^#/ || $1 == "") next
  nstop++; stop[nstop] = tolower($1)
  next
}

# ---- 3. the token stream ------------------------------------------------
$1 == "C" { cnt[$2] = $3; next }

$1 == "I" { ninst++; next }

$1 == "K" {
  layer = $2; cc = tolower($3)
  if (layer != "0") next
  ntyped++
  c = cls[cc]; r = reg[cc]
  # P115-J: a TYPED country field is a declaration, not an address, so the
  # vanity class does not apply to it. Class `cc?` still never places.
  if ((c == "cc" || c == "vanity") && r ~ /^(North America|EMEA|APAC|LATAM)$/) {
    typedreg[r] = 1
    if (typedev == "") typedev = cc
  } else {
    typedbad++
  }
  next
}

$1 == "D" {
  layer = $2; host = tolower($3)
  if (layer != "0" && layer != "1" && layer != "R") next
  nD[layer]++

  if (stopped(host)) { nstopd[layer]++; next }

  tld = host
  sub(/^.*\./, "", tld)

  c = cls[tld]
  if (c == "")       { nunk[layer]++;    next }
  if (c == "gtld")   { ngtld[layer]++;   next }
  if (c == "vanity") { nvanity[layer]++; next }
  if (c == "cc?")    { nq[layer]++; if (qev[layer] == "") qev[layer] = host; next }

  r = reg[tld]
  if (r !~ /^(North America|EMEA|APAC|LATAM)$/) { nunk[layer]++; next }

  ncc[layer]++
  seen[layer, r] = 1
  # P115-V. WHAT KIND OF ADDRESS PLACED THE ROW, CLASSIFIED STRUCTURALLY.
  # P800's rule is that a region comes from an INSTITUTION the artefact
  # names, never from a person. A ccTLD in a maintainer's email satisfies
  # "an address the tree commits" without satisfying "an institution": a
  # personal domain under `.de` places EMEA whether or not the maintainer's
  # university is in Europe. The classes below are purely structural --
  # registry-restricted suffixes, no guessing from names -- and they are
  # reported SEPARATELY so the weaker class never hides inside the total.
  k = "other"
  if (tld == "edu")                        k = "academic"
  else if (host ~ /\.ac\./)                 k = "academic"
  else if (host ~ /\.edu\./)                k = "academic"
  else if (tld == "gov" || tld == "mil")   k = "government"
  else if (host ~ /\.gov\./ || host ~ /\.gob\./) k = "government"
  klass[layer, k] = 1
  if (!((layer SUBSEP host) in hostseen)) {
    hostseen[layer, host] = 1
    if (nev[layer] + 0 < 4) ev[layer] = (ev[layer] == "" ? host : ev[layer] "," host)
    nev[layer]++
  }
  next
}

# ---------------------------------------------------------------------------
function stopped(h,   i, s, n) {
  for (i = 1; i <= nstop; i++) {
    s = stop[i]
    if (h == s) return 1
    n = length(h) - length(s)
    # suffix match on a LABEL boundary -- `europa.eu` matches `ec.europa.eu`
    # and never `noteuropa.eu`
    if (n > 0 && substr(h, n + 1) == s && substr(h, n, 1) == ".") return 1
  }
  return 0
}

# P115-P. THE REGION LIST IS BUILT BY INDEX, NEVER BY `for (r in REGIONS)`.
# awk's in-order traversal is unspecified, so the first version of this
# function emitted `EMEA|APAC` and `APAC|EMEA` for the same evidence
# depending on the hash layout. The verdict was right either way and the
# STRING was not reproducible -- and a census whose output bytes differ
# between two runs of the same input cannot be diffed against the next pass,
# which is the whole point of committing the TSV.
# P115-V. The strongest class present wins, because the placement IS
# justified by it; the weaker ones riding along change nothing.
function bestclass(layer) {
  if ((layer, "academic")   in klass) return "academic"
  if ((layer, "government") in klass) return "government"
  if ((layer, "other")      in klass) return "other"
  return "-"
}

function regionlist(layer,   i, out, n) {
  n = 0; out = ""
  for (i = 1; i <= 4; i++) {
    if ((layer, REGIONS[i]) in seen) { out = (out == "" ? REGIONS[i] : out "|" REGIONS[i]); n++ }
  }
  RL_N = n
  return (out == "" ? "-" : out)
}

END {
  # P115-M's guard. If the country map did not load, say so in the verdict
  # column instead of reporting an absence of evidence.
  if (nmap + 0 < 50) {
    print "verdict=MAPFAIL";   print "verdict_1=-";    print "rverdict=-"
    print "region_0=-";        print "regions_0=-";    print "nreg_0=0"
    print "region_1=-";        print "nreg_1=0";       print "region_r=-"
    print "nreg_r=0";          print "files=0";        print "vendored=0"
    print "struct=0";          print "root_struct=0";  print "struct_read=0"
    print "kinds=0";           print "capped=0";       print "wideline=0"
    print "dom_0=0";           print "stop_0=0";       print "gtld_0=0"
    print "vanity_0=0";        print "q_0=0";          print "unk_0=0"
    print "cc_0=0";            print "typed=0";        print "typed_ev=-"
    print "q_ev=-";            print "ev_0=-";         print "class_0=-"
    print "dom_1=0"
    print "cc_1=0";            print "ev_1=-";         print "dom_r=0"
    print "cc_r=0";            print "ev_r=-";         print "inst=0"
    exit 0
  }

  REGIONS[1] = "North America"; REGIONS[2] = "EMEA"
  REGIONS[3] = "APAC";          REGIONS[4] = "LATAM"

  # ---- the typed field, strongest evidence there is ----------------------
  tn = 0; tl = ""
  for (i = 1; i <= 4; i++) if (REGIONS[i] in typedreg) { tl = (tl == "" ? REGIONS[i] : tl "|" REGIONS[i]); tn++ }

  # ---- LAYER 0: the repository's OWN declaration -------------------------
  l0 = regionlist("0"); n0 = RL_N

  if (tn == 1)                            { verdict = "typed";       region = tl }
  else if (tn > 1)                        { verdict = "typed-split"; region = "-" }
  else if (n0 == 1)                       { verdict = "placed";      region = l0 }
  else if (n0 > 1)                        { verdict = "contested";   region = "-" }
  else if (nD["0"] + 0 > 0)               { verdict = "no-country";  region = "-" }
  else if (cnt["root_struct"] + 0 > 0)    { verdict = "no-address";  region = "-" }
  else if (cnt["struct_read"] + 0 > 0)    { verdict = "nested-only"; region = "-" }
  else                                    { verdict = "no-struct";   region = "-" }

  # ---- LAYER 1: nested declarations. A CONTRAST, never folded in --------
  l1 = regionlist("1"); n1 = RL_N
  if (n1 == 1)                { v1 = "n-placed";    r1 = l1 }
  else if (n1 > 1)            { v1 = "n-contested"; r1 = "-" }
  else if (nD["1"] + 0 > 0)   { v1 = "n-no-country"; r1 = "-" }
  else                        { v1 = "n-none";      r1 = "-" }

  # ---- LAYER R: the README. A CEILING, never folded in -------------------
  lr = regionlist("R"); nr = RL_N
  if (nr == 1)                    { rv = "r-placed";     rr = lr }
  else if (nr > 1)                { rv = "r-contested";  rr = "-" }
  else if (nD["R"] + 0 > 0)       { rv = "r-no-country"; rr = "-" }
  else if (cnt["readme"] + 0 > 0) { rv = "r-no-address"; rr = "-" }
  else                            { rv = "r-none";       rr = "-" }

  print "files="        cnt["files"] + 0
  print "vendored="     cnt["vendored"] + 0
  print "struct="       cnt["struct"] + 0
  print "root_struct="  cnt["root_struct"] + 0
  print "struct_read="  cnt["struct_read"] + 0
  print "kinds="        cnt["kinds"] + 0
  print "capped="       cnt["capped"] + 0
  print "wideline="     cnt["wideline"] + 0
  print "dom_0="        nD["0"] + 0
  print "stop_0="       nstopd["0"] + 0
  print "gtld_0="       ngtld["0"] + 0
  print "vanity_0="     nvanity["0"] + 0
  print "q_0="          nq["0"] + 0
  print "unk_0="        nunk["0"] + 0
  print "cc_0="         ncc["0"] + 0
  print "nreg_0="       n0
  print "regions_0="    l0
  print "region_0="     (region == "" ? "-" : region)
  print "verdict="      verdict
  print "typed="        ntyped + 0
  print "typed_ev="     (typedev == "" ? "-" : typedev)
  print "q_ev="         (qev["0"] == "" ? "-" : qev["0"])
  print "ev_0="         (ev["0"] == "" ? "-" : ev["0"])
  print "class_0="      bestclass("0")
  print "dom_1="        nD["1"] + 0
  print "cc_1="         ncc["1"] + 0
  print "nreg_1="       n1
  print "region_1="     r1
  print "verdict_1="    v1
  print "ev_1="         (ev["1"] == "" ? "-" : ev["1"])
  print "dom_r="        nD["R"] + 0
  print "cc_r="         ncc["R"] + 0
  print "nreg_r="       nr
  print "region_r="     rr
  print "rverdict="     rv
  print "ev_r="         (ev["R"] == "" ? "-" : ev["R"])
  print "inst="         ninst + 0
}
