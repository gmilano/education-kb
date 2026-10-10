# manifests.awk — p112 path classifier. Reads `git ls-tree -r` lines
# (mode<SP>type<SP>sha<TAB>path) and emits a dependency-closure census plus
# the shas of the Python requirement files whose BODIES stage B must read.
#
# It is a separate file so test_p112.sh can drive it directly with crafted
# path lists as well as through depclosure.sh against real repositories.

function basename(p,   n, a) { n = split(p, a, "/"); return a[n] }
function lc(s) { return tolower(s) }

# P112-C (inherits P111-C). Dependency trees committed into a repo. p111
# stripped these because they inflate a TEST count. p112 strips them for the
# same arithmetic reason -- a committed node_modules carries thousands of
# UPSTREAM package.json files, and left in, one row reads as the most
# manifest-dense repository on the shelf -- but here the strip is ALSO a
# measurement: a repo that committed its dependency tree needs no registry to
# stand up, which is the strongest form of the property this pass measures.
# So the vendor directories are counted BY NAME, not merely dropped.
function vendor_kind(p,   n, a, i, c) {
  n = split(p, a, "/")
  for (i = 1; i <= n - 1; i++) {          # directory components only
    c = a[i]
    # Dependency trees: the content of these is resolved code, so committing
    # them removes the registry from the critical path (P112-D).
    if (c == "node_modules" || c == "bower_components" || c == "jspm_packages" ||
        c == "vendor" || c == "third_party" || c == "thirdparty" ||
        c == "Pods" || c == "Godeps") return "deps"
    # Build/interpreter residue: NOT a dependency declaration, and not
    # evidence of anything. Stripped, never counted as vendored deps.
    if (c == "site-packages" || c == ".venv" || c == "venv" ||
        c == "virtualenv" || c == ".tox" || c == ".eggs") return "residue"
    if (c ~ /\.egg-info$/) return "residue"
  }
  return ""
}

# ---------------------------------------------------------------------------
# MANIFESTS. A file that DECLARES dependencies. Returns the ecosystem key.
#
# P112-A. A manifest is matched on its exact basename, never on a substring
# and never on an extension alone. `*.json` would swallow every fixture on
# this shelf; `requirements` as a substring matches docs/requirements.rst,
# which is prose about a curriculum, and that file is on this shelf.
# ---------------------------------------------------------------------------
function manifest_eco(p,   l, b) {
  b = lc(basename(p)); l = lc(p)
  if (b == "package.json")                                     return "npm"
  if (b ~ /^requirements([-_.][a-z0-9._-]+)?\.txt$/)           return "py"
  if (b == "pyproject.toml" || b == "pipfile")                 return "py"
  if (b == "setup.py" || b == "setup.cfg")                     return "py"
  if (b == "environment.yml" || b == "environment.yaml")       return "py"
  if (b == "composer.json")                                    return "php"
  if (b == "gemfile" || b ~ /\.gemspec$/)                      return "ruby"
  if (b == "go.mod")                                            return "go"
  if (b == "cargo.toml")                                        return "rust"
  if (b == "pom.xml")                                           return "maven"
  if (b == "build.gradle" || b == "build.gradle.kts")           return "gradle"
  if (b == "mix.exs")                                           return "elixir"
  if (b == "pubspec.yaml")                                      return "dart"
  if (b == "package.swift")                                     return "swift"
  if (b ~ /\.csproj$/ || b ~ /\.fsproj$/)                       return "dotnet"
  if (b == "description" && l !~ /\//)                          return "r"
  if (b == "flake.nix" || b == "default.nix" || b == "shell.nix") return "nix"
  return ""
}

# P112-N. A DEPENDENCY DECLARATION THIS INSTRUMENT CANNOT RESOLVE IS NOT AN
# ABSENT ONE. Three shapes on this shelf declare their dependencies outside
# the manifest/lock idiom entirely, and the first draft of this pass reported
# all three as `no-manifest` -- i.e. as repositories that declare nothing:
#   bazel    oppia/oppia-android, 1 213 source files, WORKSPACE + BUILD files
#   odoo     OpenEduCat/openeducat_erp, 163 source files, `__manifest__.py`
#   moodle   microsoft/o365-moodle, 352 source files, plugin `version.php`
#            declaring `$plugin->dependencies`
# Publishing those as "declares no dependencies" would be the P111-F error
# again: a figure that is both wrong and alarmist about repositories behaving
# correctly for their ecosystem. They get their own verdict, `foreign-build`,
# which makes NO reproducibility claim in either direction.
function foreign_build(p,   b, l) {
  b = lc(basename(p)); l = lc(p)
  if (b == "workspace" || b == "workspace.bazel" || b == "module.bazel" ||
      b == "build.bazel" || b ~ /\.bzl$/)                        return "bazel"
  if (b == "__manifest__.py" || b == "__openerp__.py")            return "odoo"
  if (b == "version.php")                                         return "moodle"
  if (b == "cmakelists.txt")                                      return "cmake"
  if (b == "conanfile.txt" || b == "conanfile.py")                return "conan"
  if (b == "vcpkg.json")                                          return "vcpkg"
  return ""
}

# LOCKFILES. A file that RESOLVES a manifest to exact, reproducible versions.
function lock_eco(p,   b, l) {
  b = lc(basename(p)); l = lc(p)
  if (b == "package-lock.json" || b == "npm-shrinkwrap.json" ||
      b == "yarn.lock" || b == "pnpm-lock.yaml" ||
      b == "bun.lockb" || b == "bun.lock")                      return "npm"
  if (b == "poetry.lock" || b == "uv.lock" || b == "pipfile.lock" ||
      b == "pdm.lock" || b == "conda-lock.yml" ||
      b == "requirements.lock")                                 return "py"
  if (b == "composer.lock")                                     return "php"
  if (b == "gemfile.lock")                                      return "ruby"
  if (b == "go.sum")                                            return "go"
  if (b == "cargo.lock")                                        return "rust"
  if (b == "mix.lock")                                          return "elixir"
  if (b == "pubspec.lock")                                      return "dart"
  if (b == "package.resolved")                                  return "swift"
  if (b == "packages.lock.json")                                return "dotnet"
  if (b == "renv.lock")                                         return "r"
  if (b == "flake.lock")                                        return "nix"
  if (b == "gradle.lockfile" || b == "versions.lock" ||
      l ~ /gradle\/dependency-locks\//)                         return "gradle"
  return ""
}

# P112-K. A LOCKFILE IS EVIDENCE ONLY ABOUT AN ECOSYSTEM THE REPO DECLARES.
# `lockedcnt` is counted over the ecosystems that have a MANIFEST, so a stray
# lockfile whose manifest is absent -- a Gemfile.lock left behind after the
# Gemfile was deleted, a package-lock.json under a directory whose
# package.json was moved -- cannot credit a row with reproducibility it does
# not have. The raw lock set is emitted separately as `locks=` so the gating
# is auditable rather than silent, and so the two can be compared.
#
# P112-B. ECOSYSTEMS DIFFER IN WHETHER THE MANIFEST ITSELF PINS, and treating
# them alike is the error that would make this axis useless.
#   npm/py/php/ruby/rust/... declare RANGES; without a lockfile the resolve is
#     a function of the day it runs. These are LOCKABLE.
#   maven pins its DIRECT dependencies to literal versions inside pom.xml and
#     has no lockfile in ordinary use; a pom is therefore self-pinning for
#     direct deps and resolved (not locked) for transitives. Calling it
#     `floating` would be false; calling it `pinned` would be too generous.
#     It gets its own verdict, `self-pinned`, and is never counted as locked.
#   gradle declares versions in a script and CAN lock; it is lockable.
#   go.mod names exact versions AND go.sum carries their hashes, so go is
#     lockable with go.sum as the lock -- a go.mod without a go.sum is a
#     resolve nobody verified.
function is_lockable(e) {
  return (e == "npm" || e == "py" || e == "php" || e == "ruby" || e == "go" ||
          e == "rust" || e == "gradle" || e == "elixir" || e == "dart" ||
          e == "swift" || e == "dotnet" || e == "r" || e == "nix")
}
function is_selfpinning(e) { return (e == "maven") }

# A Python requirement file whose body stage B must read (P112-F): a
# requirements.txt pinned with `==` throughout IS a lock, and no filename can
# tell you which kind you have.
function is_reqtxt(p,   b) {
  b = lc(basename(p))
  return (b ~ /^requirements([-_.][a-z0-9._-]+)?\.txt$/)
}

# P112-G. DEPLOYABLE SHAPE. A library that floats its dependencies is
# behaving correctly -- pinning is the APPLICATION's job, and a gemspec or a
# published package MUST declare ranges or it cannot be co-installed. So the
# census separates rows that ship a deployment artefact from rows that do
# not, exactly as p111 separated code-bearing rows from specifications
# (P111-F). Without this split the headline figure is alarmist about
# repositories doing the right thing.
function is_deployable(p,   b, l) {
  b = lc(basename(p)); l = lc(p)
  if (b == "dockerfile" || b ~ /^dockerfile\./ || b ~ /\.dockerfile$/) return 1
  if (b ~ /^docker-compose([-.][a-z0-9.-]+)?\.ya?ml$/)                 return 1
  if (b ~ /^compose([-.][a-z0-9.-]+)?\.ya?ml$/)                        return 1
  if (b == "procfile")                                                 return 1
  if (b == "chart.yaml")                                               return 1
  if (l ~ /^(deploy|deployment|k8s|kubernetes|charts|helm)\//)         return 1
  if (b == "vagrantfile")                                              return 1
  return 0
}

{
  # tolerate either a bare path list or full ls-tree output
  if ($0 ~ /^[0-7]{6} (blob|tree|commit) [0-9a-f]{40}\t/) {
    sha = $3
    path = substr($0, index($0, "\t") + 1)
    type = $2
  } else { sha = ""; path = $0; type = "blob" }
  if (path == "") next
  if (type != "blob") next

  files_seen++
  vk = vendor_kind(path)
  if (vk != "") {
    vendor++
    if (vk == "deps") depstree = 1
    next
  }
  files++

  e = manifest_eco(path)
  if (e != "") {
    man++
    if (!(e in ecoseen)) { ecoseen[e] = 1 }
    if (is_reqtxt(path)) {
      reqs++
      if (sha != "" && reqsha != "") print sha "\t" path > reqsha
    }
  }

  fb = foreign_build(path)
  if (fb != "") {
    foreign++
    if (!(fb in fbseen)) { fbseen[fb] = 1
      fblist = (fblist == "" ? fb : fblist "," fb) }
  }

  le = lock_eco(path)
  if (le != "") {
    lockf++
    locked[le] = 1
  }

  if (is_deployable(path)) deploy++
}
END {
  # Ecosystem list, lockable tally, locked tally -- emitted in a stable order
  # so two rows with the same ecosystems always print the same string.
  n = split("npm py php ruby go rust maven gradle elixir dart swift dotnet r nix", ord, " ")
  for (i = 1; i <= n; i++) {
    k = ord[i]
    if (k in locked) locklist = (locklist == "" ? k : locklist "," k)   # P112-K
    if (k in ecoseen) {
      ecolist = (ecolist == "" ? k : ecolist "," k)
      if (is_lockable(k)) {
        lockable++
        if (k in locked) {
          lockedcnt++
          lockedlist = (lockedlist == "" ? k : lockedlist "," k)
        }
      } else if (is_selfpinning(k)) selfpin++
    }
  }
  printf "files_seen=%d\nfiles=%d\nvendor=%d\ndepstree=%d\nman=%d\necos=%s\nlockable=%d\nlockedcnt=%d\nlockedlist=%s\nlocks=%s\nlockf=%d\nselfpin=%d\nreqs=%d\ndeploy=%d\nforeign=%d\nfbsys=%s\n", \
    files_seen+0, files+0, vendor+0, depstree+0, man+0, \
    (ecolist == "" ? "-" : ecolist), lockable+0, lockedcnt+0, \
    (lockedlist == "" ? "-" : lockedlist), (locklist == "" ? "-" : locklist), \
    lockf+0, selfpin+0, reqs+0, deploy+0, foreign+0, \
    (fblist == "" ? "-" : fblist)
}
