# Proposed, NOT APPLIED: `GPL2_PREAMBLE` for `lib/license_family.sh` + its suite

🔴 **Unverified by execution.** The execution lane was closed this pass, so this patch was
never run. It is recorded as a proposal so p198 can run it the moment the lane reopens; it is
deliberately NOT applied to `lib/`, because an unrun patch to the canonical classifier is a
worse defect than the one it fixes.

## 1. The suite needs a required GPL-2.0 case

```bash
# TRAP 2 (p197): the GPL-2.0 PREAMBLE names the Lesser GPL.  Any classifier that greps a
# WINDOW -- even a 40-line one -- returns LGPL for pristine GPL-2.0.  Proven on SPDX's own
# GPL-2.0-only.txt (17 337 B, one "Lesser" mention).  REQUIRED case, like GPL3_S13.
GPL2_PREAMBLE='                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

 Copyright (C) 1989, 1991 Free Software Foundation, Inc.

  The licenses for most software are designed to take away your freedom to share and
change it.  (Some other Free Software Foundation software is covered by the GNU Lesser
General Public License instead.)  You can apply it to your programs, too.'
check "GPL2_PREAMBLE no se clasifica como LGPL" "$(license_family "$GPL2_PREAMBLE")" "GPL-2.0"
```

## 2. The classifier must order by DOCUMENT position, not by pattern

The rule is in `family_title_line.py` in this directory: take the first line that matches any
licence-title pattern, then read the version from that line and the next non-empty one.

## 3. The rows this changes in data already stored in this KB

`p441-tree-licence-enumeration/result.2026-10-07.tsv` carries `LGPL?` in its `families`
column for four rows. **All four are `GPL-2.0`; none is LGPL.** See
`evidence/lgpl-question-resolution.2026-10-14-p197.tsv`.
