"""p217 - ACTION QP: the bilingual token table that ACTION QL's precondition needs.

This KB's shelves are bilingual (1 087 lines carry `licencia`, 130 `sin licencia`,
31 `PROPIETARIO`) and every propagation gate it has built greps English. That is why
ACTION QN was registered on a novelty claim its own history refutes - see README.md.

Each EQUIV row is ONE concept. A gate must match ANY member, not the English one.
Extend the table the first time a pass trips on a token it lacks, and record the trip.
"""

EQUIV = {
    "licence":     ("licence", "license", "licencia"),
    "no_licence":  ("no licence", "no license", "sin licencia", "no tiene licencia"),
    "proprietary": ("proprietary", "propietario", "propietaria",
                    "all rights reserved", "todos los derechos reservados",
                    "保留所有权利"),   # P421: the NO-OSI signal may not be in English
    "path":        ("path", "paths", "ruta", "rutas"),
    "sweep":       ("sweep", "barrido"),
    "reading":     ("reading", "lectura"),
    "pass":        ("pass", "pase"),
    "gate":        ("gate", "compuerta"),
}


def first_hit(tokens, shelves):
    """Return (path, lineno, line) for the first shelf line matching any token, else None."""
    for path in shelves:
        try:
            with open(path, encoding="utf-8") as fh:
                for n, line in enumerate(fh, 1):
                    low = line.lower()
                    if any(t.lower() in low for t in tokens):
                        return (path, n, line.rstrip("\n"))
        except OSError:
            continue
    return None


def already_on_shelves(concept, shelves):
    """ACTION QL's precondition. Returns the FIRST citation, or None.

    An action may not be REGISTERED on a claim that `concept` is absent until this
    returns None. If it returns a citation, the claim is false and the action must be
    re-registered on the narrower claim the citation leaves standing.
    """
    if concept not in EQUIV:
        raise KeyError(
            "no token row for %r - add one rather than falling back to English" % concept
        )
    return first_hit(EQUIV[concept], shelves)


SHELVES = (
    "agents/top.md", "agents/trending.md",
    "repos/foundations.md", "repos/trending.md",
    "verticals/solutions.md",
    "intel/market.md", "intel/trends.md",
    "compose/patterns.md",
)
