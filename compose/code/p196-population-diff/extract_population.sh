# ACTION P196-C -- re-extract the shelf slug population and diff it against p192's 472.
#
# p192's population RULE, quoted from repos/foundations.md and applied verbatim here rather
# than re-invented: "every github.com/<owner>/<repo> URL appearing in agents/top.md,
# repos/foundations.md and verticals/solutions.md, de-duplicated, with GitHub's own
# non-repository paths (topics/, orgs/, users/, ...) excluded."
#
# Why it matters: p192 derived 472, then p194 and p195 both wrote "the whole shelf" over it,
# and p195's own retraction found 4 ranked rows ABSENT from that population.  Every
# per-shelf percentage since p192 -- including p195's headline 18.8% -- divides by it.
#
# Emits a sorted, de-duplicated slug list on stdout.
set -u
PAGES="${1:?pages dir}"

# GitHub's own non-repository first path segments.  A URL whose OWNER is one of these is not
# a repository.
is_reserved_owner() {
  case "$1" in
    topics|orgs|users|sponsors|collections|features|about|pricing|settings|login|join) return 0 ;;
    marketplace|apps|enterprise|security|site|contact|notifications|explore|trending)  return 0 ;;
    search|new|organizations|account|codespaces|readme|stars|watching|dashboard)        return 0 ;;
  esac
  return 1
}
# p192 recorded ONE extraction artefact it subtracted by hand: "repos/", from an
# api.github.com URL.  Encoded as a rule so it is subtracted by the instrument, not by hand.
is_reserved_repo() {
  # p192 subtracted "repos" by hand.  v1 of THIS instrument reproduced that and then emitted
  # "repos/.." from a relative link; v2 enumerated "." and ".." and the corpus answered with
  # "repos/..." -- THREE dots.  Enumerating dot-segments is the same mistake as enumerating
  # filenames (P441): the rule is "a name with no non-dot character is not a repository".
  case "$1" in repos|repositories) return 0 ;; esac
  case "$1" in *[!.]*) return 1 ;; *) return 0 ;; esac
}

cat "$PAGES/agents/top.md" "$PAGES/repos/foundations.md" "$PAGES/verticals/solutions.md" \
| grep -oE 'github\.com/[A-Za-z0-9][-A-Za-z0-9_.]*/[-A-Za-z0-9_.]+' \
| sed 's|^github\.com/||' \
| sed 's|\.git$||' \
| while IFS=/ read -r owner repo; do
    [ -z "$owner" ] || [ -z "$repo" ] && continue
    is_reserved_owner "$owner" && continue
    is_reserved_repo  "$repo"  && continue
    # a trailing '.' or ',' swept up from prose is not part of the name
    repo="${repo%.}"; repo="${repo%,}"
    printf '%s/%s\n' "$owner" "$repo"
  done \
| sort -u
