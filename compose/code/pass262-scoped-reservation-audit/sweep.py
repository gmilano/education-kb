"""`ACTION ZI`'s online half: re-read every restrictive-graded payload and re-run both guards.

Not in `make hooks` — it needs `github.com` and `raw.githubusercontent.com`.

    python3 sweep.py <repo-root> <out.tsv>

For each slug whose grant cell `reservation_audit.harvest()` classes `RESTRICTIVE-GRADE`:

  1. `git ls-remote --symref` resolves the default branch and `HEAD` — never a guessed ref
     (`p254`: two of this pass's own population answer on `development` and `develop`).
  2. a blobless `--no-checkout` clone yields the TREE, so a missing path is distinguishable
     from a missing channel (`p261`: a `404` cannot tell those apart; a tree can).
  3. every in-tree ladder path plus the README is fetched on the resolved ref.
  4. `p261`'s `reservation_verdict_scoped()` and this pass's `reservation_verdict_v2()` both
     run, and the DELTA is the column `ACTION ZI` asked for.

🔴 Sizes are BYTES.  The first version of this sweep reported `len(decoded_text)` and
disagreed with two correct shelf cells by `4` and `2 146` — the multi-byte characters.  It
was the instrument that was wrong, and no correction was published off it.
"""

import os
import shutil
import subprocess
import sys
import tempfile
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "pass261-current-state-tier-run"))

import reservation_audit as ra            # noqa: E402
import current_state as p261              # noqa: E402

SHELVES = ("agents/top.md", "agents/trending.md", "repos/foundations.md",
           "repos/trending.md", "verticals/solutions.md", "intel/market.md",
           "intel/trends.md", "compose/patterns.md", "intel/open-gaps.md")
EXTRA_PATHS = ("README.md", "README.rst", "README.txt", "readme.md", "README")
TIMEOUT = 180


def _run(cmd):
    return subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=TIMEOUT)


def resolve(slug):
    """`(default_branch, head_sha, error)` — never a guessed ref."""
    r = _run(f"git ls-remote --symref https://github.com/{slug} HEAD")
    if r.returncode != 0:
        return None, None, r.stderr.strip()[:140]
    ref = sha = None
    for line in r.stdout.splitlines():
        if line.startswith("ref:"):
            ref = line.split()[1].replace("refs/heads/", "")
        elif "\tHEAD" in line:
            sha = line.split()[0]
    return ref, sha, None if ref else "no symref in ls-remote output"


def tree_of(slug):
    """The repository's path set, read first-hand.  `(paths, error)`."""
    d = tempfile.mkdtemp(prefix="p262-")
    try:
        r = _run(f"git clone --filter=blob:none --no-checkout --depth 1 "
                 f"https://github.com/{slug} {d}/r")
        if r.returncode != 0:
            return None, r.stderr.strip()[:140]
        t = _run(f"git -C {d}/r ls-tree -r --name-only HEAD")
        if t.returncode != 0:
            return None, t.stderr.strip()[:140]
        return set(t.stdout.splitlines()), None
    finally:
        shutil.rmtree(d, ignore_errors=True)


def fetch(slug, ref, path):
    """`(raw_bytes, status)`.  Bytes, because the size this base publishes is bytes."""
    url = f"https://raw.githubusercontent.com/{slug}/{ref}/{path}"
    try:
        with urllib.request.urlopen(url, timeout=60) as fh:
            return fh.read(), fh.status
    except Exception as exc:                                 # pragma: no cover - network
        return None, getattr(exc, "code", str(exc)[:60])


def population(root):
    """The `RESTRICTIVE-GRADE` slugs, with the other two classes counted but not probed."""
    rows, counts = [], {}
    for shelf in SHELVES:
        p = os.path.join(root, shelf)
        if os.path.exists(p):
            rows.extend(ra.harvest(p))
    for r in rows:
        counts[r[3]] = counts.get(r[3], 0) + 1
    graded = sorted({r[0] for r in rows if r[3] == ra.GRADE_RESTRICTIVE})
    return graded, counts, rows


def main(argv):
    if len(argv) < 3:
        print(__doc__)
        return 2
    root, out = argv[1], argv[2]
    tiers = p261.ladder_tiers()
    ladder = tiers["TIER_A"] + tiers["TIER_B"]
    slugs, counts, _rows = population(root)
    print(f"# grade classes: {counts}")
    print(f"# RESTRICTIVE-GRADE slugs to probe: {len(slugs)}")

    lines = ["\t".join(("slug", "ref", "head", "path", "bytes", "chars",
                        "p261_verdict", "p262_verdict", "changed", "note"))]
    for slug in slugs:
        ref, sha, err = resolve(slug)
        if not ref:
            lines.append("\t".join((slug, "", "", "", "", "", "", "NO-REF", "", err or "")))
            print(f"{slug}\tNO-REF\t{err}", flush=True)
            continue
        paths, terr = tree_of(slug)
        if paths is None:
            lines.append("\t".join((slug, ref, (sha or "")[:12], "", "", "",
                                    "", "NO-TREE", "", terr or "")))
            print(f"{slug}\tNO-TREE\t{terr}", flush=True)
            continue
        cands = [p for p in list(ladder) + list(EXTRA_PATHS) if p in paths]
        if not cands:
            lines.append("\t".join((slug, ref, (sha or "")[:12], "", "", "",
                                    "", "NO-PAYLOAD", "", f"tree={len(paths)}")))
            print(f"{slug}\tNO-PAYLOAD\ttree={len(paths)}", flush=True)
            continue
        for path in cands:
            raw, status = fetch(slug, ref, path)
            if raw is None:
                lines.append("\t".join((slug, ref, (sha or "")[:12], path, "", "",
                                        "", "FETCH-FAIL", "", str(status))))
                continue
            body = raw.decode("utf-8", "replace")
            old, new, changed = ra.verdict_delta(body, p261.reservation_verdict_scoped)
            nbytes, nchars, _d = ra.size_disagreement(raw)
            steward = ra.steward_reservation_spans(body)
            note = (f"steward_lines={','.join(map(str, steward))};"
                    f"aggregate={len(p261.aggregate_sections(body))};"
                    f"grant_phrase={ra.permissive_grant(body)}")
            lines.append("\t".join((slug, ref, (sha or "")[:12], path, str(nbytes),
                                    str(nchars), old, new, "YES" if changed else "no", note)))
            print(f"{slug}\t{path}\t{nbytes}B\t{old} -> {new}"
                  f"{'  ★CHANGED' if changed else ''}", flush=True)

    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines) + "\n")
    print(f"\n# wrote {out}: {len(lines) - 1} rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
