"""`ACTION SP` — narrow the EU AI Act subject so it binds to a JURISDICTION.

p227's `ACTION SH` run reported `7` near misses and `3` of them were VIETNAMESE
text matched to an EU subject, because the subject alternation carried the bare
phrase `high-risk`:

    (?i)(ai act|annex iii|anexo iii|alto riesgo|high-risk)

Every jurisdiction with a risk-tiered AI regime uses that phrase, so the subject
was really "any high-risk AI regime anywhere" wearing an EU label. The unit of
this subject is the `(JURISDICTION, INSTRUMENT)` pair.

Narrowing a subject pattern can only REDUCE what a gate sees, so it is done here
on evidence and never for tidiness: the falsifier is that the genuine EU records
keep matching while the Vietnamese ones stop.
"""
import re
import sys

OLD = r"(?i)(ai act|annex iii|anexo iii|alto riesgo|high-risk)"

# A jurisdiction token is REQUIRED. `high-risk` and `alto riesgo` survive only as
# corroborators, never as the subject on their own.
NEW = (r"(?i)(\bai act\b|annex\s+iii|anexo\s+iii|reg\.?\s*\(eu\)"
       r"|\beuropean union\b|\beu\b(?=[^a-z])|\bbrussels\b)")

JURISDICTION_FREE = re.compile(r"(?i)\b(viet\s?nam(ese)?|korea|taiwan|japan|china|india|"
                               r"singapore|south africa|kenya|nigeria|egypt|brazil|chile|mexico)\b")


def classify(text):
    """Return (old_fires, new_fires, other_jurisdiction)."""
    return (bool(re.search(OLD, text)),
            bool(re.search(NEW, text)),
            bool(JURISDICTION_FREE.search(text)))


def main(argv):
    records = [l.rstrip("\n") for l in open(argv[1], encoding="utf-8")
               if l.strip() and not l.startswith("#")]
    rows = []
    for t in records:
        o, n, j = classify(t)
        if o or n:
            rows.append((o, n, j, t))
    print("old_fires\tnew_fires\tother_jurisdiction\tverdict\ttext")
    kept = dropped = lost = 0
    for o, n, j, t in rows:
        if o and n:
            v = "KEPT"; kept += 1
        elif o and not n:
            v = "DROPPED-AS-INTENDED" if j else "DROPPED-REVIEW"
            dropped += 1
        else:
            v = "NEWLY-MATCHED"; lost += 1
        print("\t".join([str(o), str(n), str(j), v, t[:180]]))
    print("\n# kept=%d dropped=%d newly_matched=%d" % (kept, dropped, lost), file=sys.stderr)


if __name__ == "__main__":
    main(sys.argv)
