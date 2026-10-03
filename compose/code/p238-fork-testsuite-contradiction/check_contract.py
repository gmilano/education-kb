#!/usr/bin/env python3
"""P238 — when a fork's SOURCE is byte-identical, the test suite is the thing that forked.

Pass 38 classified ashleycribb/learnmcp-xapi as "NOT a succession -- 2 commits ahead, both
Cloud Run", reading the COMMIT SUBJECTS.  Measured at file level in pass 77, 14/14 non-test
source files are byte-identical between the fork and DavidLMS/learnmcp-xapi, and five TEST
files differ.  Deployment config does not change tests, so the tests are the finding.

This instrument asks the only question that settles which tree is self-consistent: for each
symbol a test asserts, does that symbol EXIST in the shared source?  Both suites run against
byte-identical sources, so at most one of them can describe the code that is there.

LIMIT, declared.  This is a STATIC contradiction proof, not an executed test run: installing
the suite's third-party dependencies (pytest, respx, httpx) is not available in this
environment, so "this assertion names a symbol absent from the source" is what is measured,
not "pytest reports a failure".  The two differ, and the weaker claim is the one made here.

Usage: check_contract.py <upstream_tree> <fork_tree>
"""
import re, sys, pathlib

# (label, source file, the REGEX each side's assertion requires of the source).  Taken from the
# diff, not invented.
#
# DEFECT FIXED IN THIS INSTRUMENT, and it is the reason the probes are regexes and not
# substrings.  The first build probed the bare string "_oidc_token" and reported it PRESENT in
# the shared ralph.py -- but what is present is the METHOD `_get_oidc_token`, which CONTAINS
# that name.  The upstream test asserts an ATTRIBUTE ACCESS (`plugin._oidc_token == ...`), and
# that attribute does not exist: the source assigns `self._token_cache`.  A substring probe for
# an attribute name hits the getter that wraps it, and scores a contradiction as agreement.
# Anchor on the access form (`self.` / `.`), never on the bare name.
PROBES = [
    ("atributo de cache de token OIDC", "learnmcp_xapi/plugins/ralph.py",
     {"upstream": r"self\._oidc_token\s*=", "fork": r"self\._token_cache\s*="}),
    ("casing de la ruta de statements", "learnmcp_xapi/plugins/ralph.py",
     {"upstream": r"/xapi/statements/", "fork": r"/xAPI/statements/"}),
    ("contrato de validacion de config", "learnmcp_xapi/config.py",
     {"upstream": r"LRS_ENDPOINT is required", "fork": r"LRS_KEY and LRS_SECRET are required"}),
]

def main():
    up, fork = (pathlib.Path(p) for p in sys.argv[1:3])
    rows, score = [], {"upstream": 0, "fork": 0}
    for label, srcrel, claims in PROBES:
        a, b = (up / srcrel).read_bytes(), (fork / srcrel).read_bytes()
        identical = a == b
        src = a.decode("utf-8", "replace")
        verdicts = {}
        for side, token in claims.items():
            # case-sensitive on purpose: the casing of /xAPI/ IS the disagreement
            present = re.search(token, src) is not None
            verdicts[side] = present
            if present:
                score[side] += 1
        rows.append((label, srcrel, identical, claims, verdicts))

    w = 34
    print(f"{'probe':<{w}} {'fuente identica':<16} {'upstream afirma':<34} {'fork afirma':<34}")
    for label, srcrel, identical, claims, v in rows:
        def cell(side):
            mark = "PRESENTE" if v[side] else "AUSENTE "
            return f"{mark} {claims[side]!r}"
        print(f"{label:<{w}} {'SI' if identical else 'NO':<16} {cell('upstream'):<34} {cell('fork'):<34}")

    print()
    n = len(PROBES)
    print(f"afirmaciones que el codigo COMPARTIDO sostiene:  upstream {score['upstream']}/{n}"
          f"   fork {score['fork']}/{n}")
    if score["fork"] > score["upstream"]:
        print("veredicto: el suite del FORK describe el codigo que esta ahi; el del UPSTREAM no.")
        print("           La bifurcacion no es de despliegue: es del contrato de prueba, y el")
        print("           mensaje de commit del fork ('Cloud Run deployment') no lo menciona.")
    elif score["upstream"] > score["fork"]:
        print("veredicto: el suite del upstream es el consistente.")
    else:
        print("veredicto: empate — no concluir.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
