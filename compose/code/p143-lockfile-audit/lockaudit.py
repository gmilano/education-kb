"""p143-lockfile-audit -- ACTION DO.

Recomputes every SHA-256 in `malkreide/global-education-mcp`'s `tools.lock.json`
INDEPENDENTLY of the repository's own generator, using only the algorithm that
generator documents:

    signature = {"name", "description", "inputSchema", "annotations"}
    canonical = json.dumps(signature, sort_keys=True, ensure_ascii=False)
    hash      = sha256(canonical.encode("utf-8")).hexdigest()

Two separate questions are asked, and they are NOT the same question:

  (a) INTERNAL CONSISTENCY -- does each entry's stored `hash` actually digest the
      `signature` block stored beside it? This is answerable from the lockfile
      alone and needs no execution. A mismatch here means the lockfile is
      self-inconsistent: the hash does not cover the thing it sits next to, and
      every CI `verify` that passed did so against a digest of something else.

  (b) SOURCE AGREEMENT -- does that signature block describe the tool the source
      actually declares? Answered separately, at source level, in srcagree.py.

Run: python3 -I lockaudit.py <path-to-tools.lock.json>
"""

import hashlib
import json
import sys

SIG_KEYS = ("name", "description", "inputSchema", "annotations")


def recompute(sig):
    canonical = json.dumps(sig, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def main(argv):
    lock = json.load(open(argv[0], encoding="utf-8"))
    cols = ["tool", "stored_hash", "recomputed_hash", "verdict", "sig_keys", "annotations",
            "read_only", "schema_props"]
    print("\t".join(cols))
    agree = disagree = 0
    for name in sorted(lock):
        entry = lock[name]
        stored = entry.get("hash", "")
        sig = entry.get("signature", {})
        got = recompute(sig)
        ok = (got == stored)
        agree += ok
        disagree += (not ok)
        ann = sig.get("annotations") or {}
        schema = sig.get("inputSchema") or {}
        props = schema.get("properties") or {}
        # key-set check: a hash over a DIFFERENT set of fields than the one
        # documented would still be internally consistent, so report the set.
        keyset = ",".join(sorted(sig.keys()))
        print("\t".join([
            name, stored[:16], got[:16],
            "AGREE" if ok else "DISAGREE",
            keyset,
            "YES(%d)" % len(ann) if ann else "NONE",
            str(ann.get("readOnlyHint")),
            str(len(props)),
        ]))
    print("\n# tools in lockfile: %d" % len(lock), file=sys.stderr)
    print("# hash AGREE:    %d" % agree, file=sys.stderr)
    print("# hash DISAGREE: %d" % disagree, file=sys.stderr)
    # Does every entry carry exactly the four documented fields?
    bad = [n for n in lock if tuple(sorted((lock[n].get("signature") or {}).keys()))
           != tuple(sorted(SIG_KEYS))]
    print("# entries whose signature key-set is NOT the documented four: %d %s"
          % (len(bad), bad or ""), file=sys.stderr)
    ro = [n for n in lock
          if ((lock[n].get("signature") or {}).get("annotations") or {}).get("readOnlyHint")
          is not True]
    print("# entries WITHOUT readOnlyHint=true: %d %s" % (len(ro), ro or ""), file=sys.stderr)
    return 1 if disagree else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
