#!/bin/sh
# FIXTURE (p174). NEGATIVE CONTROL: /tmp scratch files are correct and portable.
# The gate must not confuse a temporary output with the KB root.
curl -s -o /tmp/lic.$$ https://example.invalid/LICENSE
WORK=${1:-/tmp/aiact502}
rm -f /tmp/lic.$$
