#!/bin/bash
# POSITIVE control, frozen from grant-ladder/test_ladder.sh: a control suite that
# reports its own score in PROSE and exits non-zero. The word FAILED never
# appears. Must classify as `assert` - the only class meaning the instrument
# disagrees with the repository.
echo "ok   - unnamed MIT resolves by signature"
echo "7/10 controls passed"
exit 1
