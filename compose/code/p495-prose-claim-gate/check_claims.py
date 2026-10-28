#!/usr/bin/env python3
"""p495 — the prose-loss detector.

`p493` proved a full-file rewrite silently drops TABLE ROWS, and found eight by
grepping repo URLs.  `p494` proved the same rewrite drops PROSE, and that the
prose case has no key to grep for: an entire APAC regulatory paragraph (Singapore's
agentic-AI governance framework) was deleted by `p315` and nobody noticed for
~179 passes, because nobody knows to look for a fact the file no longer mentions.

This instrument supplies the missing key.  A load-bearing prose claim is registered
with a distinctive literal GREP KEY and the file that must carry it.  The gate then
re-asks, every run, the one question a rewrite cannot answer for itself: is the
claim still there?

🔴 The control that matters is ARCHIVE-ONLY.  `p494`'s Singapore paragraph was NOT
absent from the repository — `grep -ril` found it, in
`archive/2026-10-19-p315-pre-rewrite/intel-market.md`.  A detector that searches the
whole tree therefore reports the deleted claim as PRESENT and is worse than none.
A key surviving only under `archive/` is a LOSS, and is graded red.
"""
import sys, os, csv

ARCHIVE_DIRS = ("archive/", "scratchpad/")
VERDICTS = ("PRESENT", "CLAIM-LOST", "ARCHIVE-ONLY", "NO-SUCH-FILE")


def read_register(path):
    """Rows: claim_id, grep_key, required_file, pass_of_record, why_it_matters."""
    if not os.path.exists(path):
        raise SystemExit("🔴 REFUSED: no register at %s — this gate does not pass by default" % path)
    rows, seen = [], set()
    with open(path, encoding="utf-8") as fh:
        rd = csv.DictReader((l for l in fh if not l.startswith("#")), delimiter="\t")
        for r in rd:
            cid = (r.get("claim_id") or "").strip()
            key = (r.get("grep_key") or "").strip()
            tgt = (r.get("required_file") or "").strip()
            if not cid:
                raise SystemExit("🔴 REFUSED: a register row has no claim_id")
            if not key:
                raise SystemExit("🔴 REFUSED: %s has a BLANK grep_key — a blank key matches everything "
                                 "and would grade a lost claim as present" % cid)
            if not tgt:
                raise SystemExit("🔴 REFUSED: %s names no required_file" % cid)
            if cid in seen:
                raise SystemExit("🔴 REFUSED: duplicate claim_id %s — one id, one verdict" % cid)
            seen.add(cid)
            rows.append({"claim_id": cid, "grep_key": key, "required_file": tgt,
                         "pass_of_record": (r.get("pass_of_record") or "").strip(),
                         "why_it_matters": (r.get("why_it_matters") or "").strip()})
    if not rows:
        raise SystemExit("🔴 REFUSED: the register is empty — nothing was checked")
    return rows


def _flat(text):
    """Collapse every whitespace run to one space.

    🔴 Not cosmetic — it is what makes the gate usable at all. This KB hard-wraps
    prose at ~95 characters, so almost any claim worth registering crosses a line
    break: `p495` registered `T15`'s thesis and the gate reported CLAIM-LOST on a
    sentence that was sitting in the file, because the key spanned a wrap. A
    detector that forces single-line keys can only protect claims short enough to
    fit a wrap, which excludes exactly the load-bearing ones.
    """
    return " ".join(text.split())


def _contains(path, key):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return _flat(key) in _flat(fh.read())
    except OSError:
        return False


def _archive_hits(root, key):
    """Does the key survive ONLY in a pre-rewrite archive?  That is the loss signature."""
    hits = []
    for base, dirs, files in os.walk(root):
        rel = os.path.relpath(base, root).replace(os.sep, "/") + "/"
        if not any(rel.startswith(a) or ("/" + a) in ("/" + rel) for a in ARCHIVE_DIRS):
            continue
        for f in files:
            if f.endswith(".md") and _contains(os.path.join(base, f), key):
                hits.append(os.path.join(rel, f).replace("//", "/"))
    return hits


def grade(root, rows):
    out = []
    for r in rows:
        target = os.path.join(root, r["required_file"])
        if not os.path.exists(target):
            out.append(dict(r, verdict="NO-SUCH-FILE", detail=r["required_file"]))
            continue
        if _contains(target, r["grep_key"]):
            out.append(dict(r, verdict="PRESENT", detail=""))
            continue
        arch = _archive_hits(root, r["grep_key"])
        if arch:
            out.append(dict(r, verdict="ARCHIVE-ONLY", detail="survives only in: " + ", ".join(sorted(arch)[:3])))
        else:
            out.append(dict(r, verdict="CLAIM-LOST", detail="absent from the whole corpus"))
    return out


def main(argv):
    root = argv[1] if len(argv) > 1 else "."
    reg = argv[2] if len(argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "claim_register.tsv")
    results = grade(root, read_register(reg))
    bad = [r for r in results if r["verdict"] != "PRESENT"]
    for r in bad:
        print("🔴 %-14s %s — %s" % (r["verdict"], r["claim_id"], r["why_it_matters"]))
        print("   key   : %s" % r["grep_key"])
        print("   wanted: %s  (pass of record %s)" % (r["required_file"], r["pass_of_record"]))
        if r["detail"]:
            print("   %s" % r["detail"])
    print("── p495-prose-claim-gate: %d registered, %d present, %d LOST"
          % (len(results), len(results) - len(bad), len(bad)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
