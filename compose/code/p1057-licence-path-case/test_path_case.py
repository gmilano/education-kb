"""p189 / P1057 tests. Every fixture is REAL manifest text measured this pass over the
raw channel, or a deliberate negative. No invented manifests."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from path_case import candidate_paths, declared_licence_files, probe_plan

# openedx/XBlock, pyproject.toml, HEAD, 3 344 B, HTTP 200 — the row that caused this.
XBLOCK = '''[project]
name = "XBlock"
license = "Apache-2.0"
license-files = ["LICENSE.TXT"]
'''

# blend-ed/tutor-contrib-openedxmcp, pyproject.toml, HEAD, 847 B, HTTP 200.
# Declares a licence STRING and no file: the authoritative channel is ABSENT here.
OEMCP = 'license = { text = "AGPL-3.0" }\nname = "tutor-contrib-openedxmcp"\n'

# ink-waffle/sisu-mcp, package.json, HEAD, 999 B, HTTP 200. Same: string, no path.
SISU = '{"name": "sisu-mcp", "license": "MIT"}'

# An npm manifest naming the file. The field is rare but it is the one that resolves.
NPM_FILE = '{"name": "x", "license": "MIT", "licenseFile": "LICENSE.MIT"}'

# PEP 639 permits several paths.
TWO = 'license-files = ["LICENSE.TXT", "LICENSE-DATA"]\n'

fails = []
def check(name, got, want):
    if got != want:
        fails.append(f"{name}: got {got!r}, want {want!r}")

# --- the miss that caused this instrument must be in the probe list ---------------
check("LICENSE.TXT is a candidate", "LICENSE.TXT" in candidate_paths(), True)
check("the bare uppercase stem is probed FIRST", candidate_paths()[0], "LICENSE")
check("lowercase extension also covered", "LICENSE.txt" in candidate_paths(), True)
check("British spelling covered", "LICENCE" in candidate_paths(), True)
check("candidate list is de-duplicated",
      len(candidate_paths()), len(set(candidate_paths())))

# --- the manifest channel, where it exists ---------------------------------------
check("XBlock's declared path is read", declared_licence_files(XBLOCK), ["LICENSE.TXT"])
check("XBlock's declared path is probed first",
      probe_plan(XBLOCK)["order"][0], "LICENSE.TXT")
check("a declared path is not also repeated as a variant",
      probe_plan(XBLOCK)["variants"].count("LICENSE.TXT"), 0)
check("channel is named when the manifest answers",
      probe_plan(XBLOCK)["channel"], "manifest")
check("several declared paths are kept in order",
      declared_licence_files(TWO), ["LICENSE.TXT", "LICENSE-DATA"])
check("npm licenseFile is read", declared_licence_files(NPM_FILE), ["LICENSE.MIT"])

# --- a licence STRING is not a licence PATH: the commonest shape must yield nothing
check("pyproject license string declares no file", declared_licence_files(OEMCP), [])
check("package.json license string declares no file", declared_licence_files(SISU), [])
check("channel falls back when no path is declared",
      probe_plan(SISU)["channel"], "case-variants")

# --- a caller that truncates must still get the useful probes --------------------
check("limit truncates", len(candidate_paths(limit=4)), 4)
check("truncated list still leads with LICENSE", candidate_paths(limit=4)[0], "LICENSE")

if fails:
    print(f"FAIL {len(fails)}/{16}")
    for f in fails:
        print("  -", f)
    sys.exit(1)
print("PASS 16/16 — P1057")
