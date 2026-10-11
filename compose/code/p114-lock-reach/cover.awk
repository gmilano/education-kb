# cover.awk — p114 stage-2 coverage rule. Reads positions.awk output and
# answers, for every manifest in the tree: IS THERE A LOCK THAT REACHES IT?
#
# ---------------------------------------------------------------------------
# DISCIPLINES
#
# P114-A  THE UNIT IS THE (MANIFEST, DIRECTORY) PAIR, NOT THE REPOSITORY.
#   p112's unit was the repo-ecosystem: one package-lock.json anywhere made
#   `npm` locked for the whole row, however many package.json files the tree
#   held. A resolver does not work that way -- it is invoked in a directory
#   and resolves the manifest it finds there. So the denominator here is
#   MANIFESTS, and a row with one covered manifest and nine orphans is a row
#   that is 10 % pinned, not 100 %.
#
# P114-B  COVERAGE IS AN ANCESTOR RELATION, NOT PROXIMITY, AND IT IS STILL
#   GENEROUS. A lock covers a manifest sitting in its own directory or in any
#   DESCENDANT of it: that is the npm-workspaces / pnpm / cargo-workspace
#   convention, where one root lock legitimately resolves every member. It
#   does NOT cover siblings or cousins -- a lock in `examples/demo/` says
#   nothing about the manifest at the root.
#   The error direction is stated here rather than discovered later: a root
#   lock credited to a deep member may not actually list that member's
#   dependencies, so p114's reach is ALSO an upper bound on pinning. It is a
#   strictly TIGHTER one than p112's -- every row p114 moves, it moves
#   downward, and no row can read more pinned here than it did at p112.
#
# P114-C  A PINNED `requirements.txt` IS A LOCK WHERE IT SITS. P112-F
#   established that a requirements.txt pinned with `==` throughout IS a lock.
#   p112 could treat it as a repo-level fact; p114 must treat it as a
#   POSITIONAL one, so a fully pinned `ml/requirements.txt` covers `ml/` and
#   below and leaves a root `setup.py` orphaned. Supplied by the driver as
#   `-v extrapy=<dir,dir,...>` after stage B has read the bodies.
#
# P114-D  A COMMITTED DEPENDENCY TREE MAKES REACH INAPPLICABLE, NOT ZERO.
#   A repo carrying node_modules/ or a Go vendor/ needs no registry and no
#   lock to stand up (P112-D). Such a row is `vendored` and NO reach claim is
#   made about it, exactly as at p112.
#
# P114-E  NO CLAIM IS MADE WHERE p112 MADE NONE. maven-only rows stay
#   `self-pinned` and bazel/odoo/moodle-plugin rows stay `foreign-build`.
#   Inventing a reach figure for a build system this instrument does not
#   resolve would be the P111-F error in a new costume.
#
# P114-F  A LOCK IS EVIDENCE ONLY ABOUT A MANIFEST IT CAN REACH. This
#   subsumes P112-K (a lock whose ecosystem has NO manifest credits nothing)
#   and adds the case p112 cannot see: a lock whose ecosystem HAS manifests
#   but which sits BELOW every one of them credits nothing either. `locks`
#   and `locks_live` are both emitted so the gating is auditable.
#
# P114-H  THE CONTROL IS p112's OWN RULE. `-v flat=1` restores "one lock
#   anywhere counts", which is p112's P112-E rule exactly. The delta between
#   the two modes over the same 296 trees is therefore a MEASUREMENT of the
#   error p112 declared, not an assertion about it. Any row where the two
#   modes agree is a row where position never mattered.
#
# P1040  AN UNREAD ROW IS NEVER ZERO -- enforced by the driver, which never
#   calls this rule on a tree it failed to fetch.
# ---------------------------------------------------------------------------
#
# VERDICT LADDER (worst to best), deliberately parallel to p112's so the two
# passes can be cross-tabulated row by row:
#   no-manifest    nothing declares dependencies
#   foreign-build  declared in a build system not resolved here (P114-E)
#   no-reach       lockable manifests exist; NO lock reaches any of them
#   vendored       no lock reaches anything, but the tree is COMMITTED
#   partial-reach  some lockable manifests reached, others orphaned
#   self-pinned    maven only (P114-E)
#   full-reach     every lockable manifest has a lock above or beside it
#                  (above = P114-B ancestor; beside = same directory, which
#                  is all a stage-B requirements credit ever gives, P114-G)

function is_lockable(e) {
  return (e == "npm" || e == "py" || e == "php" || e == "ruby" || e == "go" ||
          e == "rust" || e == "gradle" || e == "elixir" || e == "dart" ||
          e == "swift" || e == "dotnet" || e == "r" || e == "nix")
}
function is_selfpinning(e) { return (e == "maven") }

# depth("")=0 (root), depth("a")=1, depth("a/b")=2
function depth(d,   n, a) {
  if (d == "") return 0
  return split(d, a, "/")
}

# P114-B. Does a lock at dir L reach a manifest at dir D?
function reaches(L, D) {
  if (L == D) return 1
  if (L == "") return 1                       # root lock covers the tree
  return (index(D, L "/") == 1)               # D is a descendant of L
}

BEGIN { FS = "\t"; flat = (flat == "" ? 0 : flat + 0) }

$1 == "M" { mi++; meco[mi] = $2; mdir[mi] = $3; mpath[mi] = $4; ecoseen[$2] = 1; next }
$1 == "L" { li++; leco[li] = $2; ldir[li] = $3; lockset[$2] = 1; next }
$1 == "F" { foreign++; if (!($2 in fbseen)) { fbseen[$2] = 1
              fblist = (fblist == "" ? $2 : fblist "," $2) } next }
$1 == "C" { cnt[$2] = $3 + 0; next }

END {
  # P114-C. Stage B's pinned requirement files enter as py locks AT THEIR OWN
  # DIRECTORY. Credited here, never earlier, so a run with stage B skipped
  # (the P112-F contribution control) differs by exactly these entries.
  if (extrapy != "") {
    n = split(extrapy, xp, ",")
    for (i = 1; i <= n; i++) {
      if (xp[i] == "-") continue
      li++; leco[li] = "py"; ldir[li] = (xp[i] == "/" ? "" : xp[i])
      lown[li] = 1                                 # P114-G: own directory only
      lockset["py"] = 1
      reqpin_dirs++
    }
  }

  lockable_man = 0; covered = 0; selfpin_man = 0
  deepest_orphan = -1; root_orphan = 0

  for (i = 1; i <= mi; i++) {
    e = meco[i]
    if (is_selfpinning(e)) { selfpin_man++; continue }       # P114-E
    if (!is_lockable(e))     continue
    lockable_man++

    hit = 0
    for (j = 1; j <= li; j++) {
      if (leco[j] != e) continue
      if (flat) { hit = 1; break }                           # P114-H: p112's rule
      if (j in lown) {                                       # P114-G
        if (ldir[j] == mdir[i]) { hit = 1; break }
        continue
      }
      if (reaches(ldir[j], mdir[i])) { hit = 1; break }      # P114-B
    }
    if (hit) { covered++; liveeco[e] = 1 }                   # P114-F
    else {
      orphans++
      if (!(e in orpheco)) { orpheco[e] = 1 }
      dd = depth(mdir[i])
      if (dd > deepest_orphan) deepest_orphan = dd
      if (dd == 0) root_orphan = 1
      if (orphlist == "" || length(orphlist) < 220)
        orphlist = (orphlist == "" ? mpath[i] : orphlist ";" mpath[i])
    }
  }

  # stable ordering for every emitted list
  n = split("npm py php ruby go rust maven gradle elixir dart swift dotnet r nix", ord, " ")
  for (i = 1; i <= n; i++) {
    k = ord[i]
    if (k in ecoseen)  ecolist  = (ecolist  == "" ? k : ecolist  "," k)
    if (k in lockset)  locklist = (locklist == "" ? k : locklist "," k)
    if (k in liveeco)  livelist = (livelist == "" ? k : livelist "," k)
    if (k in orpheco)  orpholist= (orpholist== "" ? k : orpholist "," k)
  }

  if (mi == 0 && foreign > 0)              verdict = "foreign-build"
  else if (mi == 0)                        verdict = "no-manifest"
  else if (lockable_man == 0 && selfpin_man > 0) verdict = "self-pinned"
  else if (lockable_man == 0)              verdict = "no-manifest"
  else if (covered >= lockable_man)        verdict = "full-reach"
  else if (covered > 0)                    verdict = "partial-reach"
  else if (cnt["depstree"] == 1)           verdict = "vendored"      # P114-D
  else                                     verdict = "no-reach"

  printf "man_total=%d\nlockable_man=%d\nselfpin_man=%d\ncovered=%d\norphans=%d\n", \
    mi+0, lockable_man+0, selfpin_man+0, covered+0, orphans+0
  printf "deepest_orphan=%d\nroot_orphan=%d\nreqpin_dirs=%d\nlocks_total=%d\n", \
    deepest_orphan, root_orphan+0, reqpin_dirs+0, li+0
  printf "ecos=%s\nlocks=%s\nlocks_live=%s\norphan_ecos=%s\n", \
    (ecolist == "" ? "-" : ecolist), (locklist == "" ? "-" : locklist), \
    (livelist == "" ? "-" : livelist), (orpholist == "" ? "-" : orpholist)
  printf "orphan_paths=%s\nfbsys=%s\nverdict=%s\n", \
    (orphlist == "" ? "-" : orphlist), (fblist == "" ? "-" : fblist), verdict
}
