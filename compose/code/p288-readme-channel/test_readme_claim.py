"""Controls for `ACTION p288`'s README channel.

The three REAL fixtures of this pass are controls 1-3 and they are quoted VERBATIM from the
bodies fetched on 2026-10-18, because a fixture paraphrased is a fixture that stops
reproducing.  The collision arm is the reason the verb anchor exists.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from readme_claim import README_PATHS, channel_verdict, posture, readme_claim

FAIL = []


def check(name, got, want):
    if got != want:
        FAIL.append(f"{name}: got {got!r}, want {want!r}")


# ---------------------------------------------------------------- the real fixtures
# 1. anastasasenov/bbmcps -- readme.md (LOWERCASE), 1 582 B, line 84.  Tree = 9 files,
#    NONE_IN_TREE.  A grant CLAIMED and not SERVED.
BBMCPS = """# bbmcps

Blackboard MCP Server

### License

This project is open-source and available under the MIT License.
"""
check("bbmcps/claim", readme_claim(BBMCPS), ("CLAIM", "MIT"))
check("bbmcps/verdict", channel_verdict(readme_claim(BBMCPS), None), "DANGLING-CLAIM")
check("bbmcps/posture", posture("DANGLING-CLAIM").split(" ")[0], "ASK")

# 2. hdronamraju/sped-agent -- README.md, 12 689 B, line 53.  A grant REFUSED.
SPED = """## License

(c) 2026 hdronamraju. All rights reserved. You're welcome to view and try this project and
to give feedback; please ask before reusing the code.
"""
check("sped-agent/claim", readme_claim(SPED), ("RESERVATION", None))
check("sped-agent/verdict", channel_verdict(readme_claim(SPED), None), "RESERVED-NO-PAYLOAD")
check("sped-agent/posture", posture("RESERVED-NO-PAYLOAD").split(" ")[0], "STOP")

# 3. yoyoconnor/BlackboardMCP -- README.md, 4 551 B, no licence sentence anywhere.
BBMCP_RO = """# blackboard-mcp

Read-only MCP server for Blackboard Learn. It never submits, posts or changes anything.

## Limits worth knowing

Treat this cookie like your password. Don't commit it.
"""
check("BlackboardMCP/claim", readme_claim(BBMCP_RO), ("NO-CLAIM", None))
check("BlackboardMCP/verdict", channel_verdict(readme_claim(BBMCP_RO), None), "SILENT-NO-PAYLOAD")

# 4. AaronGrace978/EduHelp -- payload READ (AGPL-3.0, 34 523 B), README asserts nothing.
check("EduHelp/verdict", channel_verdict(("NO-CLAIM", None), "AGPL-3.0"), "PAYLOAD-ONLY")

# ---------------------------------------------------------------- collision controls
# 🔴 THE ONE THIS PASS WOULD HAVE FAILED.  "MIT RAISE" appeared in p288's own North America
# search leg, and an education README naming it is entirely ordinary.
check("collision/MIT-RAISE",
      readme_claim("Produced with Day of AI, AASA and MIT RAISE."), ("NO-CLAIM", None))
check("collision/MIT-Media-Lab",
      readme_claim("Curriculum adapted from the MIT Media Lab."), ("NO-CLAIM", None))
check("collision/MIT-OCW",
      readme_claim("Problem sets follow MIT OpenCourseWare 6.034."), ("NO-CLAIM", None))
# A POINTER is not a claim: the payload channel answers this one, not the README channel.
check("collision/pointer", readme_claim("See LICENSE for details."), ("NO-CLAIM", None))
# p280's vendored class must not reach the verdict through the README either.
check("collision/vendored-path",
      readme_claim("Third-party notices in ui/node_modules/react/LICENSE."),
      ("NO-CLAIM", None))
# 🔴 Guards the POSTFIX arm specifically: the institution strip must run BEFORE it, or
# "MIT RAISE licensed material" reads as an MIT grant.
check("collision/postfix-institution",
      readme_claim("This unit is MIT RAISE licensed material."), ("NO-CLAIM", None))
# The markdown-link reduction must not invent a claim out of a bare link to a file.
check("collision/link-pointer",
      readme_claim("See [LICENSE](./LICENSE) for terms."), ("NO-CLAIM", None))
# p287's AIProf, in its VERBATIM markdown-link form.
check("claim/AIProf-verbatim",
      readme_claim("This project is [MIT](./LICENSE) licensed."), ("CLAIM", "MIT"))
# A bare family token with no verb is not an assertion.
check("collision/bare-token", readme_claim("MIT, Apache-2.0 and GPL are all OSI families."),
      ("NO-CLAIM", None))

# ---------------------------------------------------------------- direction controls
check("claim/apache", readme_claim("Licensed under the Apache License, Version 2.0"),
      ("CLAIM", "Apache-2.0"))
check("claim/agpl-before-gpl", readme_claim("This is released under the GNU AGPLv3."),
      ("CLAIM", "AGPL-3.0"))
check("claim/lgpl-before-gpl", readme_claim("Distributed under the LGPL v3."),
      ("CLAIM", "LGPL-3.0"))
check("claim/british-spelling", readme_claim("This project is licenced under the MIT licence."),
      ("CLAIM", "MIT"))
check("claim/colon-form", readme_claim("License: BSD-3-Clause"), ("CLAIM", "BSD"))
# A RESERVATION outranks a family token in the same body -- the dangerous direction.
check("reservation/outranks",
      readme_claim("Available under the MIT License.\n\nAll rights reserved."),
      ("RESERVATION", None))
check("reservation/viewing-only", readme_claim("Viewing only. Do not redistribute."),
      ("RESERVATION", None))

# A README that disagrees with its own payload is a CONFLICT, not an agreement.
check("conflict/direction", channel_verdict(("CLAIM", "MIT"), "GPL-3.0"), "CLAIM-CONFLICT")
check("agree/direction", channel_verdict(("CLAIM", "MIT"), "MIT"), "AGREE")
# p287's AIProf shape, now gradeable: README says MIT, payload is verbatim GPL-3.0.
check("conflict/AIProf", channel_verdict(readme_claim("This project is MIT licensed."),
                                         "GPL-3.0"), "CLAIM-CONFLICT")
check("no-readme", channel_verdict(readme_claim(None), None), "NO-CHANNEL")

# ---------------------------------------------------------------- the ladder itself
# 🔴 The lowercase rung is the reason this instrument exists: bbmcps serves `readme.md` and
# answers 404 at `README.md` on every ref.
check("ladder/has-lowercase", "readme.md" in README_PATHS, True)
check("ladder/has-uppercase", "README.md" in README_PATHS, True)
check("ladder/superset-of-pass262",
      set(("README.md", "README", "README.rst", "README.txt", "readme.md")).issubset(
          set(README_PATHS)), True)

if FAIL:
    print(f"🔴 p288-readme-channel: {len(FAIL)} control(s) FAILED")
    for f in FAIL:
        print("   " + f)
    sys.exit(1)
print("🟢 p288-readme-channel: all controls pass")
