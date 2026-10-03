#!/bin/bash
# P191 -- the SPEC-LICENSE sweep (action 3 of pass 67).
#
# CHANNEL NOTE, measured this pass and it decides the method:
#   raw.githubusercontent.com/<slug>/HEAD/<path>  -> 200  (works, this is the probe)
#   api.github.com/repos/<slug>                   -> 403  (blocked by the egress proxy)
#   github.com/<slug>/tree/HEAD/ via curl         -> 400  (blocked)
#   github.com/<slug>/tree/HEAD/ via WebFetch     -> 200  (the ONLY directory listing open)
#
# So version-subdirectory ENUMERATION is not scriptable here: it was done with WebFetch and
# its result is frozen into targets.tsv, which is why the target list is data and not a
# glob.  Each row carries the artefact TYPE (document|software), because pass 68 measured
# that the regime splits on that axis and on the publisher -- not on "being a standard".
#
# TSV: slug . path . label . type . http . verdict . family . bytes . quote
while IFS=$'\t' read -r slug path label type; do
  [ -z "${slug:-}" ] && continue
  code=$(curl -s -o /tmp/spec.$$ -w "%{http_code}" --max-time 25 "https://raw.githubusercontent.com/$slug/HEAD/$path")
  if [ "$code" != "200" ]; then
    # P187's lesson, applied to this instrument: a 404 at a NAME is not an absence of
    # cession.  Separate the two causes before writing either one, by asking whether the
    # REPOSITORY answers at all.  REPO-UNREACHABLE and ABSENT are different facts and this
    # KB has already published one as the other once.
    rc=$(curl -s -o /dev/null -w "%{http_code}" --max-time 20 "https://raw.githubusercontent.com/$slug/HEAD/README.md")
    if [ "$rc" != "200" ]; then
      printf '%s\t%s\t%s\t%s\t%s\tREPO-UNREACHABLE\t-\t-\t-\n' "$slug" "$path" "$label" "$type" "$code"
    else
      printf '%s\t%s\t%s\t%s\t%s\tABSENT-AT-THIS-NAME\t-\t-\t-\n' "$slug" "$path" "$label" "$type" "$code"
    fi
  else
    out=$(python3 classify_spec.py < /tmp/spec.$$)
    printf '%s\t%s\t%s\t%s\t200\t%s\n' "$slug" "$path" "$label" "$type" "$out"
  fi
  rm -f /tmp/spec.$$
done < "${1:-targets.tsv}"
