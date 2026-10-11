#!/usr/bin/env bash
# P121 suite. Fully offline: every assertion runs against fixtures or the
# committed pages. No network.
set -u
ROOT="${1:-/tmp/education-kb}"
HERE="$(cd "$(dirname "$0")" && pwd)"
pass=0; fail=0
ok(){ pass=$((pass+1)); printf '  ok   %s\n' "$1"; }
no(){ fail=$((fail+1)); printf '  FAIL %s\n' "$1"; }
chk(){ if [ "$2" = "$3" ]; then ok "$1"; else no "$1 (got '$2' want '$3')"; fi; }
T=$(mktemp -d)

# ---------- ACTION O: the extractor ----------
cat > "$T/f1.md" <<'FIX'
| [`a/b`](https://github.com/a/b) | 🟡 GPL-3 | deps are COMMITTED, so it stands |
| [`c/d`](https://github.com/c/d) | **0BSD** ✅ | fine |
| [`e/f`](https://github.com/e/f) | **LGPLv3** / BSD-2-Clause | ok |
| [`g/h`](https://github.com/g/h) | ECL-2.0 ("consists of the Apache 2.0 license, modified") | ok |
| [`i/j`](https://github.com/i/j) | AGPL-3.0 AGPL AGPL | dup test |
| no slug here | MIT | skipped |
FIX
R=$("$HERE/extract-v6.sh" "$T/f1.md")
chk "COMMITTED does not yield an MIT claim" "$(echo "$R" | awk -F'\t' '$3=="a/b"{print $4}')" "GPL-3.0"
chk "0BSD matched as 0BSD, not BSD"          "$(echo "$R" | awk -F'\t' '$3=="c/d"{print $4}')" "0BSD"
chk "LGPLv3 normalised to LGPL-3.0"          "$(echo "$R" | awk -F'\t' '$3=="e/f"{print $4}')" "LGPL-3.0,BSD-2-Clause"
chk "quoted 'Apache 2.0' is not a claim"     "$(echo "$R" | awk -F'\t' '$3=="g/h"{print $4}')" "ECL-2.0"
chk "comma-joined dedup guard kills the repeat" "$(echo "$R" | awk -F'\t' '$3=="i/j"{print $4}')" "AGPL-3.0,AGPL"
chk "a non-table line yields no row"         "$(echo "$R" | grep -c 'no slug')" "0"

# the v4-only control must LOSE the 0BSD row -- the reason v6 widens as well as anchors
R4=$("$HERE/extract-v4.sh" "$T/f1.md")
chk "v4 (anchor only) drops the 0BSD row"    "$(echo "$R4" | awk -F'\t' '$3=="c/d"{print $4}')" ""
R3=$("$HERE/extract-noanchor.sh" "$T/f1.md")
chk "v3 (no anchor) invents MIT on a/b"      "$(echo "$R3" | awk -F'\t' '$3=="a/b"{print $4}' | grep -c MIT)" "1"

# ---------- ACTION P: the inline correction guard ----------
cat > "$T/f2.md" <<'FIX'
| repo | licence | note |
|---|---|---|
| [`k/l`](https://github.com/k/l) | 🔴 **NO GRANT — no licence file** ⚠️ **was 🟢 MIT** | ok |
| [`m/n`](https://github.com/m/n) | 🟢 MIT | ok |
FIX
R=$(HERE="$HERE" T="$T" python3 -I - <<'GUARD' | tail -1
import os, importlib.util, sys
spec = importlib.util.spec_from_file_location("cp", os.path.join(os.environ["HERE"], "crosspage.py"))
cp = importlib.util.module_from_spec(spec)
sys.argv = ["crosspage.py", os.environ["T"]]
spec.loader.exec_module(cp)
cp.ROOT = os.environ["T"]; cp._cache.clear()
print("YES" if (cp.in_correction_table("f2.md", 3) and not cp.in_correction_table("f2.md", 4)) else "NO")
GUARD
)
chk "inline 'was X' row is a correction, plain row is not" "$R" "YES"

# the WIDENED guard must still let a real defect through: a plain recommendation
# row carrying only a licence token and a reuse verdict is NOT a correction.
cat > "$T/f3.md" <<'FIX'
| repo | licence | reuse |
|---|---|---|
| [`o/p`](https://github.com/o/p) | 🟢 MIT | 🟢 yes |
| [`q/r`](https://github.com/q/r) | 🔴 **no licence file** — author claim only | 🔴 no |
| address | manifest says | committed file says |
| [`s/t`](https://github.com/s/t) | 🟢 MIT | 🔴 AGPL-3.0 |
FIX
R2=$(HERE="$HERE" T="$T" python3 -I - <<'GUARD2' | tail -1
import os, importlib.util, sys
spec = importlib.util.spec_from_file_location("cp", os.path.join(os.environ["HERE"], "crosspage.py"))
cp = importlib.util.module_from_spec(spec)
sys.argv = ["crosspage.py", os.environ["T"]]
spec.loader.exec_module(cp)
cp.ROOT = os.environ["T"]; cp._cache.clear()
plain   = cp.in_correction_table("f3.md", 3)   # must be False -- a real defect can surface
inline  = cp.in_correction_table("f3.md", 4)   # must be True
hdrrow  = cp.in_correction_table("f3.md", 6)   # must be True (under `committed file says`)
print("YES" if (not plain and inline and hdrrow) else f"NO plain={plain} inline={inline} hdr={hdrrow}")
GUARD2
)
chk "widened guard suppresses disclosures but NOT real defects" "$R2" "YES"

# ---------- repairs are present and idempotent ----------
chk "freelingo repaired in agents/top.md" \
  "$(grep -c 'artcc/freelingo`](https://github.com/artcc/freelingo) | \*\*165\*\* | 164 | 🔴 \*\*AGPL-3.0\*\*' "$ROOT/agents/top.md")" "1"
chk "i-educar repaired in verticals/solutions.md" \
  "$(grep -c 'i-educar`](https://github.com/portabilis/i-educar) | SIS (LATAM, BR) | \*\*718\*\* | 🔴 \*\*GPL-2.0\*\*' "$ROOT/verticals/solutions.md")" "1"
chk "unitime repaired to Apache-2.0" \
  "$(grep -c 'UniTime/unitime) | timetabling | \*\*350\*\* | 🟢 \*\*Apache-2.0\*\*' "$ROOT/verticals/solutions.md")" "1"
chk "pupilfirst repaired to MIT" \
  "$(grep -c 'pupilfirst) | LMS | \*\*979\*\* | 🟢 \*\*MIT\*\*' "$ROOT/verticals/solutions.md")" "1"
chk "course-tencent-cloud repaired to GPL-2.0" \
  "$(grep -c 'course-tencent-cloud) | MOOC (APAC, CN) | \*\*1 173\*\* | 🔴 \*\*GPL-2.0\*\*' "$ROOT/verticals/solutions.md")" "1"
chk "repair.py is idempotent"  "$(python3 -I "$HERE/repair.py"  "$ROOT" | grep -c '^REPAIRED')" "0"
chk "repair2.py is idempotent" "$(python3 -I "$HERE/repair2.py" "$ROOT" | grep -c '^REPAIRED')" "0"
chk "no doubled correction marker was introduced" \
  "$(grep -ohE '⚠️ \*\*was [^|]*⚠️ \*\*was' "$ROOT"/agents/*.md "$ROOT"/repos/*.md "$ROOT"/verticals/*.md "$ROOT"/intel/*.md "$ROOT"/compose/patterns.md | wc -l)" "0"

# ---------- ACTION Q: normalisation ----------
Q=$(HERE="$HERE" python3 -I - <<'NORM' | tail -1
import os, importlib.util
spec = importlib.util.spec_from_file_location("mq", os.path.join(os.environ["HERE"], "manifest_q.py"))
mq = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(mq)
except SystemExit:
    pass
n = mq.norm
tests = [("GPL v3","GPL-3.0"),("AGPL 3","AGPL-3.0"),("MANIFEST:GPLv3","GPL-3.0"),
         ("GPL-3.0-or-later","GPL-3.0"),("Elastic-2.0","ELASTIC-2.0"),
         ("ElasticLicense-2.0-NOT-OSS","ELASTIC-2.0"),("BSD-3-Clause","BSD-3")]
bad = [f"{a}->{n(a)}!={b}" for a, b in tests if n(a) != b]
print("OK" if not bad else ";".join(bad))
NORM
)
chk "manifest licence normalisation" "$Q" "OK"

# ---------- data files exist and are non-trivial ----------
for f in claims.v6.tsv action-p.tsv action-q.tsv action-n.tsv verify.2026-10-11.tsv; do
  if [ -s "$HERE/$f" ]; then ok "$f present and non-empty"; else no "$f missing/empty"; fi
done
chk "ACTION N probed 4 addresses"  "$(wc -l < "$HERE/action-n.tsv")" "4"
chk "ACTION N: all 4 ungranted"    "$(grep -c 'NO-GRANT-FOUND' "$HERE/action-n.tsv")" "4"
chk "live verification ran on 8 defect addresses" "$(wc -l < "$HERE/verify.2026-10-11.tsv")" "8"

# ---------- the corrected-domain sweep is now clean ----------
chk "ACTION P corrected-domain defects = 0" \
  "$(python3 -I "$HERE/crosspage.py" "$ROOT" | awk -F': *' '/^DEFECT rows/{print $2}')" "0"

rm -rf "$T"
echo
echo "$pass passed / $fail failed"
[ "$fail" -eq 0 ]
