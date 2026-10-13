#!/bin/sh
# FIXTURE (p174). NEGATIVE CONTROL. Every path here is narrative about a defect that
# was already fixed, and the gate must NOT fail on it:
# ABSOLUTE path /tmp/education-kb/... and this pass's clone is at /home/user/education-kb,
#     . /home/user/education-kb/compose/code/lib/license_family.sh
ROOT="${1:-$(cd "$(dirname "$0")/../../.." && pwd)}"
