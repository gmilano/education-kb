# lib/reqname.awk -- IS THIS BASENAME A PYTHON REQUIREMENT FILE?
#
# ONE definition, consumed with a second `-f` by every pass that needs it, so
# the next correction does not have to be remembered in two places. That is
# P237, and this file exists because the debt P237 named came due.
#
# HISTORY, because the rule's shape is the finding.
#
# p112 (`manifests.awk`) and p114 (`positions.awk`) each carried their own
# copy of an ANCHORED rule:
#
#     ^requirements([-_.][a-z0-9._-]+)?\.txt$
#
# Anchoring at the FRONT was deliberate and still is: it is what keeps
# `docs/requirements.rst` -- prose about a curriculum, and really on this
# shelf -- from being read as a manifest. But it also refuses the other half
# of the same convention, the PREFIXED spelling:
#
#     dev_requirements.txt   system_requirements.txt   latest_requirements.txt
#
# p114 found this by hand while verifying a single row, sized it over all 296
# addresses (198 files seen, 8 missed, 5 rows affected), declared it as
# `Gap 404`, and did NOT fix it -- because P237 forbids forking a shared
# classifier and the correction belonged with the rule, not with one pass.
#
# THE WIDENED RULE (`P116-P`). An optional prefix segment is allowed before
# `requirements`, on the same separators the suffix already allows:
#
#     ^([a-z0-9._-]+[-_.])?requirements([-_.][a-z0-9._-]+)?\.txt$
#
# What it now matches that it did not:   dev_requirements.txt
#                                        system_requirements.txt
#                                        latest_requirements.txt
#                                        test-requirements.txt
# What it still refuses:                 requirements.rst   requirements.md
#                                        requirements.txt.bak
#                                        myrequirements.txt      <- no separator
#                                        requirements/base.txt   <- a directory
#
# The `myrequirements.txt` exclusion is the point of requiring the separator.
# Without it the prefix group swallows any word ending in the literal string
# and the rule stops being about the convention at all.
#
# ERROR DIRECTION. Widening can only ever ADD a file the old rule refused, so
# a figure computed with this rule is >= the same figure computed with the old
# one. For the reach axis that means coverage can only rise: no row loses a
# verdict it held under the narrow rule. Stated here so it is not rediscovered.

function is_reqname(b) {
  return (b ~ /^([a-z0-9._-]+[-_.])?requirements([-_.][a-z0-9._-]+)?\.txt$/)
}
