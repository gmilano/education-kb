# classify.awk — p111 path classifier. Reads `git ls-tree -r` lines
# (mode<SP>type<SP>sha<TAB>path) and emits counts plus the CI blob shas.
#
# It is a separate file so test_p111.sh can drive it directly with crafted
# path lists as well as through vsurface.sh against real repositories.

function basename(p,   n, a) { n = split(p, a, "/"); return a[n] }
function lc(s) { return tolower(s) }

# P111-C. Dependency trees committed into a repo. These carry thousands of
# UPSTREAM test files; left in, the repo with a committed node_modules reads
# as the best-tested row on the shelf.
function is_vendor(p,   n, a, i, c) {
  n = split(p, a, "/")
  for (i = 1; i <= n - 1; i++) {          # directory components only
    c = a[i]
    if (c == "node_modules" || c == "bower_components" || c == "jspm_packages" ||
        c == "vendor" || c == "third_party" || c == "thirdparty" ||
        c == "site-packages" || c == ".venv" || c == "venv" || c == "virtualenv" ||
        c == "Pods" || c == ".tox" || c == ".eggs" || c == "Godeps") return 1
    if (c ~ /\.egg-info$/) return 1
  }
  return 0
}

# P111-A. A path COMPONENT, never a substring. `grep -i test` over a tree
# matches docs/testimonials.rst, src/latest.py, contest/, protest.js and
# greatest.h -- every one of which is a false positive, and all five are on
# this shelf.
function in_test_dir(p,   n, a, i, c) {
  n = split(p, a, "/")
  for (i = 1; i <= n - 1; i++) {
    c = lc(a[i])
    if (c == "test" || c == "tests" || c == "spec" || c == "specs" ||
        c == "__tests__" || c == "testing" || c == "unittest" ||
        c == "unittests" || c == "e2e" || c == "testcases" ||
        c == "test_suite" || c == "testsuite") return 1
  }
  return 0
}

# A test FILE by naming convention. Separator-anchored on purpose (P111-A):
# `test_*` and `test-*`, never a bare `test*` prefix.
function is_test_name(b,   l) {
  l = lc(b)
  if (l ~ /^test_/ || l ~ /^test-/) return 1
  if (l ~ /^tests?\.(py|js|ts|rb|go|php|sh)$/) return 1
  if (l ~ /_test\.(py|js|ts|tsx|go|rb|php|c|cc|cpp|java|kt|rs|sh|exs?)$/) return 1
  if (l ~ /_tests\.(py|js|ts|go|rb|php|rs)$/) return 1
  if (l ~ /_spec\.(rb|js|ts|py|php)$/) return 1
  if (l ~ /\.test\.(js|jsx|ts|tsx|mjs|cjs|py|dart)$/) return 1
  if (l ~ /\.spec\.(js|jsx|ts|tsx|mjs|cjs|rb|dart)$/) return 1
  if (l ~ /test[s]?\.(java|kt|cs|scala|php)$/) return 1   # FooTest.java, FooTests.cs
  if (l == "conftest.py") return 1
  return 0
}

# Test RUNNER CONFIG is evidence that a suite is meant to be run, but it is
# not itself a test, so it is counted on its own axis (P111-E).
function is_test_cfg(b,   l) {
  l = lc(b)
  if (l == "pytest.ini" || l == "tox.ini") return 1
  if (l ~ /^phpunit\.xml(\.dist)?$/) return 1
  if (l ~ /^behat\.yml(\.dist)?$/) return 1
  if (l == ".rspec") return 1
  if (l ~ /^jest\.config\.(js|ts|mjs|cjs|json)$/) return 1
  if (l ~ /^vitest\.config\.(js|ts|mjs)$/) return 1
  if (l ~ /^karma\.conf\.js$/) return 1
  if (l ~ /^\.mocharc\.(json|ya?ml|js)$/) return 1
  if (l ~ /^nose\.cfg$/) return 1
  # NOT pyproject.toml / package.json / setup.cfg: those are build manifests
  # that merely CAN carry a [tool.pytest] table. Counting them makes almost
  # every Python and Node repo on the shelf read as having a suite.
  return 0
}

# Source extensions. Used ONLY to answer "is there code here to test at all"
# (P111-F): a specification, an awesome-list or a curriculum dataset with no
# tests is correctly bare and is NOT a risk.
function is_src(b,   l) {
  l = lc(b)
  return (l ~ /\.(py|js|jsx|mjs|cjs|ts|tsx|java|php|rb|go|rs|c|cc|cpp|cxx|h|hpp|cs|kt|kts|swift|scala|m|mm|pl|lua|dart|ex|exs|vue|svelte|jl|r|erl|hs|clj|groovy|f90|sql|ipynb)$/)
}

# CI. The file set, and which SYSTEM each belongs to.
function ci_system(p,   l, b) {
  l = lc(p); b = lc(basename(p))
  if (l ~ /^\.github\/workflows\/[^\/]+\.ya?ml$/) return "gha"
  if (b == ".gitlab-ci.yml" || l ~ /^\.gitlab\/ci\/.*\.ya?ml$/) return "gitlab"
  if (b == ".travis.yml") return "travis"
  if (l ~ /^\.circleci\/config\.ya?ml$/) return "circle"
  if (b == "jenkinsfile" || l ~ /^\.jenkins\//) return "jenkins"
  if (b == "azure-pipelines.yml" || b == "azure-pipelines.yaml") return "azure"
  if (b == "appveyor.yml" || b == ".appveyor.yml") return "appveyor"
  if (b == ".drone.yml") return "drone"
  if (b == ".woodpecker.yml" || l ~ /^\.woodpecker\//) return "woodpecker"
  if (b == "bitbucket-pipelines.yml") return "bitbucket"
  if (l ~ /^\.buildkite\/.*\.ya?ml$/) return "buildkite"
  if (l ~ /^\.teamcity\//) return "teamcity"
  return ""
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
  if (is_vendor(path)) { vendor++; next }
  files++

  b = basename(path)

  if (in_test_dir(path) || is_test_name(b)) {
    # P111-B. A fixture or a snapshot inside tests/ is not a test either, but
    # it IS part of the suite, so it is counted here and not split further.
    tests++
  } else if (is_src(b)) {
    src++
  }
  if (is_test_cfg(b)) testcfg++

  s = ci_system(path)
  if (s != "") {
    ci++
    if (!(s in sysseen)) { sysseen[s] = 1; syslist = (syslist == "" ? s : syslist "," s) }
    if (sha != "" && cisha != "") print sha "\t" path > cisha
  }
}
END {
  printf "files_seen=%d\nfiles=%d\nvendor=%d\nsrc=%d\ntests=%d\ntestcfg=%d\nci=%d\nsystems=%s\n", \
    files_seen+0, files+0, vendor+0, src+0, tests+0, testcfg+0, ci+0, (syslist == "" ? "-" : syslist)
}
