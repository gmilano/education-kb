# select.awk -- TREE -> the bounded set of blobs whose BODIES decide this row.
#
# Input : `git ls-tree -r <ref>` lines, i.e. "<mode> blob <sha>\t<path>".
# Output: "<sha>\t<kind>\t<path>" for every selected blob, then a final
#         "#tally\t<files>\t<stripped>\t<selected>\t<capped>" line.
#
# P113-A  A DECLARATION AND A SENTENCE ARE NOT THE SAME EVIDENCE. A dependency
#   manifest, an environment template, a compose file and a Modelfile DECLARE
#   what a program binds to. A README DESCRIBES it. Both are read, both are
#   reported, and only the first kind may set a verdict. This is p742's
#   body-versus-reference discipline and p752's prose-versus-committed-results
#   discipline applied to provider binding instead of to licences.
#
# P113-B  THE README IS READ AT THE ROOT ONLY. `examples/*/README.md` is a
#   tutorial for one example, not a statement about the repository, and on a
#   monorepo there are dozens of them. Depth-0 only, so the prose column means
#   one and the same thing on every row.
#
# P113-C  BUILD RESIDUE IS STRIPPED WITHOUT CREDIT, AND THE STRIP IS COUNTED.
#   A `node_modules/.../package.json` or a `.venv/.../pyproject.toml` is a
#   machine's leftovers: it would make a repository look as though it declared
#   hundreds of providers it never chose. p112 credited a committed dependency
#   tree because reproducibility is helped by it; provider BINDING is not, so
#   here the strip earns nothing. The count is emitted so a reader can see how
#   much of the tree was discarded.
#
# P113-D  THE SELECTION IS CAPPED AND THE CAP IS REPORTED. A monorepo with 400
#   package.json files would spend the whole budget on one row. The cap is a
#   per-row limit on blobs read, and a row that hit it is flagged, because a
#   capped row's "no provider found" is a weaker statement than an uncapped
#   row's.
BEGIN { FS = "\t"; cap = (CAP + 0 > 0 ? CAP + 0 : 60) }

{
  # "<mode> blob <sha>" in $1, path in $2.
  split($1, h, " ")
  if (h[2] != "blob") next
  sha  = h[3]
  path = $2
  files++

  if (path ~ /(^|\/)(node_modules|vendor|\.venv|venv|site-packages|\.tox|dist|build|third_party|bower_components|\.git)\//) { stripped++; next }
  if (path ~ /\.egg-info\//)                                                                                               { stripped++; next }

  n = path; sub(/.*\//, "", n)
  depth = (path ~ /\//)

  kind = ""
  if (n ~ /^requirements[^\/]*\.txt$/ ||
      n == "pyproject.toml" || n == "setup.py" || n == "setup.cfg" ||
      n == "Pipfile" || n == "package.json" || n == "go.mod" ||
      n == "Cargo.toml" || n == "pom.xml" || n == "composer.json" ||
      n == "pubspec.yaml" || n == "Gemfile" || n == "build.gradle" ||
      n == "build.gradle.kts" || n ~ /^environment\.ya?ml$/ ||
      n ~ /^conda[^\/]*\.ya?ml$/)                                   kind = "manifest"
  else if (n ~ /^\.?env($|[._-])/ && n !~ /\.(py|js|ts|sh|md)$/)    kind = "env"
  else if (n ~ /^(docker-)?compose[^\/]*\.ya?ml$/)                  kind = "compose"
  else if (n == "Modelfile" || n ~ /\.?Modelfile$/)                 kind = "modelfile"
  else if (!depth && n ~ /^README(\.md|\.rst|\.txt)?$/)             kind = "readme"   # P113-B
  else next

  if (selected >= cap) { capped = 1; next }                                           # P113-D
  selected++
  printf "%s\t%s\t%s\n", sha, kind, path
}

END { printf "#tally\t%d\t%d\t%d\t%d\n", files, stripped, selected, (capped ? 1 : 0) }
