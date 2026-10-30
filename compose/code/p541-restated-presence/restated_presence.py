#!/usr/bin/env python3
"""p541 — Gap 540-A: the mirror of `gate-absence`.  A RESTATED PRESENCE.

`gate-absence` (p279) and `gate-capability-absence` (p392) both catch an
ABSENCE the base's own files refute.  Nothing on this base caught the
opposite and more common failure: a pass presenting as a DISCOVERY an address
the base already holds.

The measurement that registered it, and the one that justifies the cost:

  p540  four of five candidates its search legs produced were already in the
        tree (open-webui's branding clause, opetushallitus/koski's EUPL grant,
        ECL-2.0 as a family, GarethManning/education-agent-skills).
  p541  TWENTY of twenty.  Five of five supply candidates from the mandated
        agent/trending legs, and fifteen of fifteen policy and adoption claims
        from the mandated four-region sweep.  See ../../../intel/open-gaps.md.

At 20/20 the mandated query set is not a research instrument any more, it is a
restatement generator, and the only thing standing between it and the page is
whether the pass happens to run four greps by hand.  This makes that check
mechanical.

🔵 WHY IT READS A GIT REF AND NOT THE WORKING TREE.

Gap 540-A asked for "a gate that fails if the address already appears in the
curated pages".  Run against the WORKING tree after a pass has written its
rows, that predicate fails on every genuinely new address the pass just filed
-- the pass's own row is a presence.  A gate that is red exactly when the work
is good is a gate that gets switched off, which is how `gate-region-headings`
sat in no target for 45 passes (p338).

So the corpus is read with `git show <ref>:<path>`, default `HEAD`, which is
the tree as it was BEFORE this pass wrote anything.  The gate is therefore
runnable at any point in the pass -- before the write as a research filter,
after it as a standing check -- and means the same thing both times.

🔵 ROLE, NOT FILE.  p536 established that WHERE an address renders decides what
it means, and this instrument grades on the same axis:

  FILED    in a table row on a curated page .... 🔴 the base has SHELVED it
  PROSE    on a curated page, no table row ..... 🔴 the base has WRITTEN about it
  HISTORY  only trending/open-gaps ............. 🟡 owned but unfiled: PROMOTION
  ARCHIVE  only archive/ — a DELETED page ...... 🟢 not a restatement: RECOVERY
  BACKLOG  only evidence/ or code — MEASURED ... 🟢 not a restatement: PROMOTION
  ABSENT   nowhere ............................. 🟢 NEW

The ARCHIVE row is the distinction this instrument's own author got wrong
first.  A hand `grep -rl Claw-ED .` at p541 returned thirty-one paths, twenty
of them under `archive/`, and read as overwhelming evidence of a restatement.
It is not: an address surviving only in `archive/` is a page the base has
DELETED, and re-finding it is a recovery that p495's `gate-prose-claims` calls
a LOSS when it does not happen.  Grading those as restatements would punish
exactly the work the base wants.

p538's key/payload separation is kept: `address` is the spelling as written,
`match_key` is lower-cased for set arithmetic and never leaves this file as an
address.  GitHub redirects on case, so the key must fold and the payload must
not.
"""

import os
import re
import subprocess
import sys

# The nine committed pages, with the roles of ingest/address-ledger.py (p530).
CURATED = [
    "agents/top.md",
    "repos/foundations.md",
    "verticals/solutions.md",
    "intel/market.md",
    "intel/trends.md",
    "compose/patterns.md",
]
HISTORY = [
    "agents/trending.md",
    "repos/trending.md",
    "intel/open-gaps.md",
]

# Same shape as the ledger's, so the two instruments cannot disagree about what
# an address IS.  Owner and repo are captured separately: a bare repo name is
# not an address, and matching on one is this gate's CLASS 1 false positive.
ADDR = re.compile(r"github\.com/([A-Za-z0-9][A-Za-z0-9_.-]*)/([A-Za-z0-9][A-Za-z0-9_.-]*)")
STRIP_SUFFIX = re.compile(r"\.git$")

VERDICTS = ("FILED", "PROSE", "HISTORY", "ARCHIVE", "BACKLOG", "ABSENT")
# FILED and PROSE are the two that may not reach a page unregistered.
RED = ("FILED", "PROSE")

# A reason must say something.  p471 graded gap LANGUAGE; this is the same idea
# at one field's width: a registration that says "dup" has not been reasoned.
PLACEHOLDER = re.compile(r"^(todo|tbd|n/?a|dup(licate)?|known|seen|-+|\?+)\.?$", re.I)
MIN_REASON = 20


def norm(owner, repo):
    """The comparison KEY.  Never an address -- see p538."""
    return f"{owner.lower()}/{STRIP_SUFFIX.sub('', repo).lower()}"


def parse_candidate(text):
    """Accept `owner/repo` or any github.com URL spelling of it.

    Returns (address_as_written, match_key) or None.  A bare repo name with no
    owner is refused rather than guessed at: CLASS 1.
    """
    text = text.strip()
    if not text:
        return None
    m = ADDR.search(text)
    if m:
        owner, repo = m.group(1), m.group(2)
    else:
        bare = text.strip("/")
        if bare.count("/") != 1:
            return None
        owner, repo = bare.split("/")
        if not owner or not repo:
            return None
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", owner):
            return None
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]*", repo):
            return None
    repo = STRIP_SUFFIX.sub("", repo)
    return f"{owner}/{repo}", norm(owner, repo)


def is_table_row(line):
    """p277's rendered-table predicate: a row is a line whose first non-space
    character is a pipe.  A pipe later in a sentence is prose."""
    return line.lstrip().startswith("|")


def read_ref(root, ref, path):
    """The committed text of one page, or None when the ref lacks it.

    Reading through `git show` rather than the filesystem is the whole point --
    see the module docstring.  `ref=None` reads the working tree instead, which
    the suite uses and a pass should not.
    """
    if ref is None:
        full = os.path.join(root, path)
        if not os.path.exists(full):
            return None
        with open(full, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    try:
        out = subprocess.run(
            ["git", "-C", root, "show", f"{ref}:{path}"],
            capture_output=True, check=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return out.stdout.decode("utf-8", errors="replace")


def index_corpus(root, ref=None, extra_history=()):
    """match_key -> set of roles, over the nine committed pages.

    `extra_history` names further paths to grade as HISTORY-weight (evidence,
    archive) when a caller wants them indexed; by default they are NOT read,
    and an address found nowhere in the nine is ARCHIVE-or-ABSENT, which
    `classify` separates with its own cheap scan.
    """
    index = {}
    for path in CURATED:
        text = read_ref(root, ref, path)
        if text is None:
            continue
        for line in text.splitlines():
            role = "FILED" if is_table_row(line) else "PROSE"
            for owner, repo in ADDR.findall(line):
                index.setdefault(norm(owner, repo), set()).add(role)
    for path in list(HISTORY) + list(extra_history):
        text = read_ref(root, ref, path)
        if text is None:
            continue
        for owner, repo in ADDR.findall(text):
            index.setdefault(norm(owner, repo), set()).add("HISTORY")
    return index


def classify(match_key, index, archive_keys=frozenset(), backlog_keys=frozenset()):
    """The predicate.  Worst role wins:
    FILED > PROSE > HISTORY > ARCHIVE > BACKLOG > ABSENT."""
    roles = index.get(match_key, set())
    for role in ("FILED", "PROSE", "HISTORY"):
        if role in roles:
            return role
    if match_key in archive_keys:
        return "ARCHIVE"
    if match_key in backlog_keys:
        return "BACKLOG"
    return "ABSENT"


def read_registrations(path):
    """`restatements.tsv`: address<TAB>reason.

    Returns (by_key, problems).  A registration whose reason is empty, a
    placeholder or shorter than MIN_REASON does not count as registered --
    otherwise the gate is cleared by typing a hyphen.
    """
    by_key, problems = {}, []
    if not path or not os.path.exists(path):
        return by_key, problems
    with open(path, encoding="utf-8") as fh:
        for n, raw in enumerate(fh, 1):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            parts = line.split("\t")
            if parts and parts[0].strip().lower() == "address":
                continue  # p277: a header is not data
            if len(parts) < 2:
                problems.append(f"line {n}: needs address<TAB>reason")
                continue
            parsed = parse_candidate(parts[0])
            if not parsed:
                problems.append(f"line {n}: {parts[0]!r} is not an owner/repo address")
                continue
            reason = parts[1].strip()
            if not reason or PLACEHOLDER.match(reason):
                problems.append(f"line {n}: {parsed[0]} reason is a placeholder, not a reason")
                continue
            if len(reason) < MIN_REASON:
                problems.append(
                    f"line {n}: {parsed[0]} reason is {len(reason)} chars, "
                    f"minimum {MIN_REASON}")
                continue
            by_key[parsed[1]] = reason
    return by_key, problems


def grade(candidates, index, registrations, archive_keys=frozenset(),
          backlog_keys=frozenset()):
    """One row per candidate.  `ok` is False only for an unregistered red."""
    rows = []
    for raw in candidates:
        parsed = parse_candidate(raw)
        if not parsed:
            rows.append({"raw": raw, "address": None, "match_key": None,
                         "verdict": "UNPARSEABLE", "registered": None, "ok": False})
            continue
        address, key = parsed
        verdict = classify(key, index, archive_keys, backlog_keys)
        reason = registrations.get(key)
        ok = verdict not in RED or reason is not None
        rows.append({"raw": raw, "address": address, "match_key": key,
                     "verdict": verdict, "registered": reason, "ok": ok})
    return rows


def outside_scan(root, ref=None, self_dir=None):
    """The two non-curated arms: (archive_keys, backlog_keys).

    `archive/` holds pages this base has DELETED, so an address surviving only
    there is a RECOVERY -- p495's `gate-prose-claims` calls failing to recover
    one a LOSS.  `evidence/`, `ingest/` and `compose/code/` hold addresses this
    base has MEASURED but never filed, which is a PROMOTION off a known
    backlog.  Those are different instructions to a successor, so they are
    different verdicts.  p541's first run conflated them.

    Walked on the filesystem rather than through the ref because both trees are
    append-only by convention, so a walk is one pass over the directory instead
    of thousands of `git show` calls.

    🔵 CLASS 6, and this gate found it by failing on its own author.  p541's
    first run graded `UFPA-LAMIC/EduAcess` as already-held, on the strength of
    exactly one occurrence: the fixture in this instrument's OWN test file.  An
    instrument that walks `compose/code/` indexes its own test data as corpus,
    so every address a suite quotes becomes a false presence -- and the suites
    on this base quote real rows deliberately (p392). Test files are therefore
    not corpus, and neither is the instrument's own directory.
    """
    archive_keys, backlog_keys = set(), set()
    nine = set(CURATED) | set(HISTORY)
    self_dir = os.path.abspath(self_dir or os.path.dirname(os.path.abspath(__file__)))
    arms = (("archive", archive_keys),
            ("evidence", backlog_keys),
            ("compose/code", backlog_keys),
            ("ingest", backlog_keys),
            ("README.md", backlog_keys))
    for sub, sink in arms:
        base = os.path.join(root, sub)
        if os.path.isfile(base):
            paths = [base]
        elif os.path.isdir(base):
            paths = [os.path.join(dirpath, f)
                     for dirpath, _, files in os.walk(base) for f in files]
        else:
            continue
        for full in paths:
            rel = os.path.relpath(full, root)
            if rel in nine:
                continue
            # CLASS 6: a suite's fixtures are not findings.
            if os.path.basename(full).startswith("test_"):
                continue
            if os.path.abspath(full).startswith(self_dir + os.sep):
                continue
            try:
                with open(full, encoding="utf-8", errors="replace") as fh:
                    text = fh.read()
            except (OSError, UnicodeError):
                continue
            for owner, repo in ADDR.findall(text):
                sink.add(norm(owner, repo))
    # An address in BOTH arms is an archive recovery first: the deleted page is
    # the stronger signal, because it was once judged good enough to shelve.
    backlog_keys -= archive_keys
    return archive_keys, backlog_keys


ICON = {"FILED": "🔴", "PROSE": "🔴", "HISTORY": "🟡", "ARCHIVE": "🟢",
        "BACKLOG": "🟢", "ABSENT": "🟢", "UNPARSEABLE": "🔴"}

MEANING = {
    "FILED": "already a table row on a curated page — the base has SHELVED this",
    "PROSE": "already written about on a curated page — the base OWNS this claim",
    "HISTORY": "in trending/open-gaps only — owned but unfiled: PROMOTE, do not re-discover",
    "ARCHIVE": "only on a DELETED page in archive/ — a RECOVERY, not a restatement",
    "BACKLOG": "measured in evidence/ or code, never filed — a PROMOTION off the backlog",
    "ABSENT": "not on this base — genuinely new",
    "UNPARSEABLE": "not an owner/repo address",
}


def main(argv):
    import argparse
    ap = argparse.ArgumentParser(
        description="p541 — grade candidate addresses against the COMMITTED tree")
    ap.add_argument("candidates", nargs="*",
                    help="owner/repo or github.com/owner/repo")
    ap.add_argument("--root", default=".", help="repository root")
    ap.add_argument("--ref", default="HEAD",
                    help="git ref to read the nine pages from (default HEAD); "
                         "'WORKTREE' reads the working tree, which self-matches")
    ap.add_argument("--from-file", help="one candidate per line")
    ap.add_argument("--registrations", default=None,
                    help="restatements.tsv (default <instrument dir>/restatements.tsv)")
    ap.add_argument("--tsv", help="write the graded rows here")
    args = ap.parse_args(argv)

    cands = list(args.candidates)
    if args.from_file:
        with open(args.from_file, encoding="utf-8") as fh:
            cands += [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    if not cands:
        ap.error("no candidates given")

    ref = None if args.ref == "WORKTREE" else args.ref
    reg_path = args.registrations
    if reg_path is None:
        reg_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "restatements.tsv")
    registrations, problems = read_registrations(reg_path)

    index = index_corpus(args.root, ref=ref)
    if not index:
        print(f"🔴 no addresses indexed from ref {args.ref!r} — wrong --root, or a bad ref",
              file=sys.stderr)
        return 2
    archive_keys, backlog_keys = outside_scan(args.root, ref=ref)
    rows = grade(cands, index, registrations, archive_keys, backlog_keys)

    print(f"corpus: {len(index)} addresses over {len(CURATED) + len(HISTORY)} "
          f"pages at ref {args.ref!r}; {len(archive_keys)} on deleted pages, "
          f"{len(backlog_keys)} measured-but-unfiled")
    print("")
    for r in rows:
        shown = r["address"] or r["raw"]
        print(f"{ICON[r['verdict']]} {r['verdict']:<11} {shown}")
        print(f"   {MEANING[r['verdict']]}")
        if r["registered"]:
            print(f"   registered restatement: {r['registered']}")
    counts = {}
    for r in rows:
        counts[r["verdict"]] = counts.get(r["verdict"], 0) + 1
    print("")
    print("  ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    if args.tsv:
        with open(args.tsv, "w", encoding="utf-8") as fh:
            fh.write("address\tmatch_key\tverdict\tregistered_reason\tok\n")
            for r in rows:
                fh.write("\t".join([
                    r["address"] or r["raw"], r["match_key"] or "-", r["verdict"],
                    (r["registered"] or "-").replace("\t", " "),
                    "yes" if r["ok"] else "no"]) + "\n")
        print(f"wrote {args.tsv}")

    for p in problems:
        print(f"🔴 registrations: {p}", file=sys.stderr)
    bad = [r for r in rows if not r["ok"]]
    if bad or problems:
        print("", file=sys.stderr)
        for r in bad:
            print(f"🔴 {r['verdict']} and unregistered: {r['address'] or r['raw']}",
                  file=sys.stderr)
        print(f"🔴 p541-restated-presence: {len(bad)} unregistered restatement(s), "
              f"{len(problems)} registration problem(s)", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
