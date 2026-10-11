# positions.awk — p114 stage-1 classifier. Reads `git ls-tree -r` lines
# (mode<SP>type<SP>sha<TAB>path), or a bare path list, and emits the POSITION
# of every dependency declaration in the tree:
#
#   M <TAB> eco <TAB> dir <TAB> path     a manifest, and WHERE it sits
#   L <TAB> eco <TAB> dir <TAB> path     a lockfile, and WHERE it sits
#   R <TAB> sha <TAB> dir <TAB> path     a requirements.txt whose BODY stage B reads
#   F <TAB> sys <TAB> dir <TAB> path     a foreign build declaration
#   V <TAB> kind<TAB> -   <TAB> path     a stripped vendor/residue path
#   D <TAB> -   <TAB> -   <TAB> path     a deployment artefact
#   C <TAB> key <TAB> value             scalar counts
#
# WHY A SEPARATE FILE, AND WHY POSITIONS RATHER THAN TALLIES. p112 asked
# whether a lockfile EXISTS for each ecosystem the repo declares. Its own
# README states the error that buys (P112-E): one lockfile anywhere in the
# tree credits every manifest of that ecosystem, so in a monorepo with forty
# package.json files and one root package-lock.json the figure is generous,
# and "every figure this script produces is an UPPER BOUND on pinning".
#
# An upper bound with an unmeasured gap is not a decision input. To measure
# the gap you need to know not whether a lock exists but WHERE it sits
# relative to each manifest -- so this stage throws away no position, and the
# coverage rule lives in cover.awk where it can be swapped for p112's own
# rule and the difference MEASURED (P114-H).
#
# The classification tables below are p112's, copied verbatim and deliberately
# NOT re-derived: if this pass is to say anything about p112's rows, it must
# agree with p112 about what a manifest IS. Any divergence here would show up
# as reach error and be attributed to the wrong cause.

function lc(s) { return tolower(s) }
function basename(p,   n, a) { n = split(p, a, "/"); return a[n] }

# dir("a/b/pkg.json") = "a/b";  dir("pkg.json") = "" (the repository root)
function dirname(p,   i) {
  i = length(p)
  while (i > 0 && substr(p, i, 1) != "/") i--
  return (i == 0) ? "" : substr(p, 1, i - 1)
}

# P112-C, inherited. A committed dependency tree carries thousands of UPSTREAM
# manifests; left in, one row reads as the most manifest-dense repo on the
# shelf. Dependency trees are counted BY NAME (they are the strongest form of
# reproducibility, P112-D); build residue is stripped with no credit.
function vendor_kind(p,   l) {
  l = lc(p)
  if (l ~ /(^|\/)node_modules\//)        return "deps"
  if (l ~ /(^|\/)vendor\//)              return "deps"
  if (l ~ /(^|\/)bower_components\//)    return "deps"
  if (l ~ /(^|\/)third_party\//)         return "deps"
  if (l ~ /(^|\/)\.venv\//)              return "residue"
  if (l ~ /(^|\/)venv\//)                return "residue"
  if (l ~ /(^|\/)site-packages\//)       return "residue"
  if (l ~ /(^|\/)\.tox\//)               return "residue"
  if (l ~ /\.egg-info\//)                return "residue"
  if (l ~ /(^|\/)build\/lib\//)          return "residue"
  if (l ~ /(^|\/)\.git\//)               return "residue"
  return ""
}

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

function foreign_build(p,   b) {
  b = lc(basename(p))
  if (b == "workspace" || b == "workspace.bazel" || b == "module.bazel" ||
      b == "build.bazel" || b ~ /\.bzl$/)                        return "bazel"
  if (b == "__manifest__.py" || b == "__openerp__.py")            return "odoo"
  if (b == "version.php")                                         return "moodle"
  if (b == "cmakelists.txt")                                      return "cmake"
  if (b == "conanfile.txt" || b == "conanfile.py")                return "conan"
  if (b == "vcpkg.json")                                          return "vcpkg"
  return ""
}

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

function is_reqtxt(p,   b) {
  b = lc(basename(p))
  return (b ~ /^requirements([-_.][a-z0-9._-]+)?\.txt$/)
}

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
    print "V\t" vk "\t-\t" path
    next
  }
  files++

  d = dirname(path)

  e = manifest_eco(path)
  if (e != "") {
    man++
    print "M\t" e "\t" d "\t" path
    if (is_reqtxt(path)) {
      reqs++
      print "R\t" (sha == "" ? "-" : sha) "\t" d "\t" path
    }
  }

  fb = foreign_build(path)
  if (fb != "") { foreign++; print "F\t" fb "\t" d "\t" path }

  le = lock_eco(path)
  if (le != "") { lockf++; print "L\t" le "\t" d "\t" path }

  if (is_deployable(path)) { deploy++; print "D\t-\t-\t" path }
}
END {
  print "C\tfiles_seen\t" files_seen+0
  print "C\tfiles\t"      files+0
  print "C\tvendor\t"     vendor+0
  print "C\tdepstree\t"   depstree+0
  print "C\tman\t"        man+0
  print "C\tlockf\t"      lockf+0
  print "C\treqs\t"       reqs+0
  print "C\tdeploy\t"     deploy+0
  print "C\tforeign\t"    foreign+0
}
