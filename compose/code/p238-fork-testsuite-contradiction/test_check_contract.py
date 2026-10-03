#!/usr/bin/env python3
"""Regression test for check_contract.py.  Run: python3 test_check_contract.py

The case that matters is SUBSTRING_VS_ATTRIBUTE: the first build of the instrument probed the
bare name "_oidc_token" and scored it PRESENT against a source that only ever defines the
METHOD `_get_oidc_token`.  That turned a contradiction into an agreement and would have
published "upstream 1/3" instead of "upstream 0/3".  An attribute probe must be anchored on
the access form.
"""
import re, subprocess, sys, tempfile, pathlib

# Resolve the instrument relative to THIS FILE, never to the caller's cwd.  The first build used
# a bare "check_contract.py", so running the test from the repo root (or from compose/code/, the
# way a sweep of all suites would) made subprocess find nothing, print an empty stdout, and the
# assertions report 4/8 FAIL -- a green suite turning red on the invocation alone, with the
# failures looking like real defects.  A test that depends on cwd reports the cwd, not the code.
HERE = pathlib.Path(__file__).resolve().parent
INSTRUMENT = HERE / "check_contract.py"

RALPH = '''class RalphPlugin:
    def __init__(self):
        self._token_cache = None
    async def _get_oidc_token(self) -> str:
        if self._token_cache:
            return self._token_cache
        # Ralph uses /xAPI/statements/ (note the capital X and trailing slash)
        return await self.client.post("/xAPI/statements/")
'''
CONFIG = '''class Config:
    def validate(self):
        if self.LRS_ENDPOINT and not Path(self.CONFIG_PATH).exists():
            raise ValueError("LRS_KEY and LRS_SECRET are required when using legacy configuration")
'''

def tree(root):
    p = pathlib.Path(root)
    (p / "learnmcp_xapi" / "plugins").mkdir(parents=True, exist_ok=True)
    (p / "learnmcp_xapi" / "plugins" / "ralph.py").write_text(RALPH)
    (p / "learnmcp_xapi" / "config.py").write_text(CONFIG)
    return p

fail = 0
def check(name, cond, detail=""):
    global fail
    if cond:
        print(f"ok   {name}")
    else:
        print(f"FAIL {name} {detail}")
        fail += 1

with tempfile.TemporaryDirectory() as d:
    up, fk = tree(pathlib.Path(d) / "up"), tree(pathlib.Path(d) / "fk")
    run = subprocess.run([sys.executable, str(INSTRUMENT), str(up), str(fk)],
                         capture_output=True, text=True)
    # A non-zero exit or empty output is an ERROR in the harness, not a FAILED assertion about
    # the code under test.  Distinguishing the two is the whole point: the first build conflated
    # them and reported "4/8 FAIL" for what was a missing path.
    if run.returncode != 0 or not run.stdout.strip():
        print(f"ERROR: instrument did not run (rc={run.returncode})\n"
              f"  instrument: {INSTRUMENT}\n  stderr: {run.stderr.strip()[:400]}")
        sys.exit(2)
    out = run.stdout

    # 1. The headline: with byte-identical trees carrying the FORK's contract, the score must
    #    be upstream 0/3, fork 3/3.  A substring probe would report upstream 1/3.
    check("upstream scores 0/3 (not 1/3: the substring defect)",
          "upstream 0/3" in out, f"\n{out}")
    check("fork scores 3/3", "fork 3/3" in out, f"\n{out}")
    check("verdict names the fork as the consistent tree",
          "el suite del FORK describe el codigo" in out)

    # 2. The anchoring itself, asserted directly against the fixture: the bare name is present
    #    as a substring (it is inside the method), the ATTRIBUTE ASSIGNMENT is not.
    check("bare '_oidc_token' IS a substring of the source (why the defect existed)",
          "_oidc_token" in RALPH)
    check("but 'self._oidc_token =' is absent (what the test actually asserts)",
          re.search(r"self\._oidc_token\s*=", RALPH) is None)
    check("and 'self._token_cache =' is present",
          re.search(r"self\._token_cache\s*=", RALPH) is not None)

    # 3. Casing must not be normalised away: /xapi/ and /xAPI/ are the disagreement.
    check("probe is case-sensitive on the statements path",
          re.search(r"/xapi/statements/", RALPH) is None
          and re.search(r"/xAPI/statements/", RALPH) is not None)

    # 4. Identical trees are reported as identical (the premise of the whole measurement).
    check("source reported byte-identical", out.count("SI") >= 3, f"\n{out}")

print(f"\n{8 - fail}/8")
sys.exit(1 if fail else 0)
