"""`ACTION XN` (p250) — the `maia` class: a truncation that lands on a REAL
repository, which every grant-side gate here agrees with.

`p250` measured the instance: `TouchRefletz/maia` and `TouchRefletz/maia.edu`
are two different live repositories whose existence, default branch, grant
family, byte count AND pinned licence sha all agree — the sha because stock
`AGPL-3.0` text names no holder, so it collides across unrelated projects.  No
payload check can separate them.  XN's observation is that the only remaining
discriminator is the SHELF TEXT: one address is a strict prefix of the other.

🔴 **XN prescribed the rule at LINE scope and that scope does not trip its own
falsifier.** Measured at p251: on `agents/top.md` the stump is row `45` and the
real row is `44` — one per table row, so no line holds both.  The detection
scope therefore has to be the FILE, and the LINE is what EXEMPTS a pair: a pass
that documents a truncation writes both forms on the same line, as `p250` did.

The second measured constraint is the false-positive population.  A bare
strict-prefix rule at file scope returns `223` pairs over these eight shelves,
and most are not slugs at all: `main/LICENSE` vs `main/LICENSE.md` is a pair of
RAW-URL path fragments, because a branch name sits where an owner would.  So
the rule is a conjunction of four things, each measured rather than assumed.
"""
import re

# A harvest of the same shape as `p228`'s `SLUG_RE` after `p250`'s repair:
# greedy repo group, `.` kept in the class and OUT of the terminator.
SLUG = re.compile(
    r"(?<![A-Za-z0-9._/-])([A-Za-z0-9][A-Za-z0-9_-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)"
    r"(?=[)\s`,;:'\"\]]|$)")

# Where a branch, a directory or an archive member sits in the owner slot.
# These are the names measured on these shelves at p251, not a guess.
NON_OWNER = {
    "main", "master", "develop", "HEAD", "refs", "heads", "blob", "tree", "raw",
    "agents", "repos", "intel", "compose", "verticals", "evidence", "archive",
    "ingest", "code", "lib", "docs", "fixtures", "notebooks", "topics",
    "dados", "itens", "resultados", "packages", "python", "package",
    "dist-info", "site-packages", "src", "app", "apps",
}

def harvest(line):
    """Every slug-shaped address on one line, in order."""
    return [(m.group(1) + "/" + m.group(2)).rstrip(".") for m in SLUG.finditer(line)]

def pair_class(short, long):
    """How the longer address continues past the shorter one."""
    cont = long[len(short):]
    if cont.startswith("."):
        return "DOT-SUFFIX", cont
    if cont[0] in "-_":
        return "SEPARATOR", cont
    return "ALNUM", cont

def published_as_url(slug, text):
    """Is `slug` itself published as a github.com address?

    🔴 The naive `("github.com/" + slug) in text` test reports `yes` for every
    stump, because `github.com/JushBJJ/Mr.-Ranedeer-AI-Tutor` CONTAINS
    `github.com/JushBJJ/Mr`.  Measured at p251 on this base's own shelves; the
    terminator is the fix.
    """
    return re.search(r"github\.com/" + re.escape(slug) + r"(?=[)\s`,;:'\"\]]|$)", text) is not None

# A pass that documents a truncation says so IN WORDS on the line that carries
# the stump — `p250` wrote "the stump," and `p247` wrote "harvests to".  The
# gate must still RETURN those pairs (`ACTION XN`'s falsifier is that the `maia`
# pair trips), but it must not FAIL on text a pass wrote on purpose, so the
# annotation splits `REFUSE` from `REFUSE-ANNOTATED`.
ANNOTATION = re.compile(r"stump|truncat|harvests? to|collapse|404s|dangling", re.I)

def collisions(text):
    """Every prefix pair in one shelf file, with its verdict.

    Verdicts:
      `IGNORED-PATH-FRAGMENT` — the owner slot holds a branch or a directory
      `REFUSE`   — a DOT-SUFFIX stump that appears on at least one line where
                   no longer form of it appears: a live truncation
      `DOCUMENTED` — every occurrence of the stump shares a line with a longer
                   form: a pass that wrote the defect down on purpose
      `WARN`     — `-`/`_`/alnum continuation: `moodle/moodle` and
                   `moodle/moodle-docker` are ordinarily two real repositories
    """
    lines = text.splitlines()
    per_line = [harvest(l) for l in lines]
    names = sorted({s for ls in per_line for s in ls})
    out = []
    for short in names:
        for long in names:
            if short == long or not long.startswith(short):
                continue
            if short.split("/")[0] != long.split("/")[0]:
                continue
            klass, cont = pair_class(short, long)
            if short.split("/")[0] in NON_OWNER:
                verdict = "IGNORED-PATH-FRAGMENT"
            elif klass != "DOT-SUFFIX":
                verdict = "WARN"
            else:
                bare = [i + 1 for i, ls in enumerate(per_line)
                        if short in ls and not any(x != short and x.startswith(short) for x in ls)]
                if not bare:
                    verdict = "DOCUMENTED"
                elif all(ANNOTATION.search(lines[i - 1]) for i in bare):
                    verdict = "REFUSE-ANNOTATED"
                else:
                    verdict = "REFUSE"
            bare_lines = [i + 1 for i, ls in enumerate(per_line)
                          if short in ls and not any(x != short and x.startswith(short) for x in ls)]
            out.append({"short": short, "long": long, "class": klass, "continuation": cont,
                        "verdict": verdict, "bare_lines": bare_lines,
                        "short_published_as_url": published_as_url(short, text)})
    return out

def refusals(text):
    """Only the UNANNOTATED ones: what a gate may fail on."""
    return [r for r in collisions(text) if r["verdict"] == "REFUSE"]

def flagged(text):
    """Every prefix collision the rule returns, annotated or not — this is the
    set `ACTION XN`'s falsifier is about."""
    return [r for r in collisions(text) if r["verdict"].startswith("REFUSE")]

def line_scope_collisions(text):
    """XN's literal prescription, kept so the pass can show it MISSES `maia`."""
    out = []
    for i, line in enumerate(text.splitlines(), 1):
        names = sorted(set(harvest(line)))
        for a in names:
            for b in names:
                if a != b and b.startswith(a) and a.split("/")[0] == b.split("/")[0]:
                    out.append({"line": i, "short": a, "long": b})
    return out
