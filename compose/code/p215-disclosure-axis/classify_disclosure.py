#!/usr/bin/env python3
"""P215 -- what does a connector DISCLOSE about the contractual plane?

Pass 72 (trend 566) found that terms-of-use disclosure has started travelling as a FILE IN
THE REPO, and called it "an axis of selection that neither the licence nor the write gate
shows".  It did not sweep it.  This instrument does.

The axis is NOT about tone, and not about whether a project is careful.  It is about which
DECLARATIONS are present in the text, in this order of strength:

  D1  DISCLOSURE-WITH-STATUTE-AND-TOU  ToU quoted verbatim + the admission that the provider
                                       may treat the channel as a violation + a NAMED statute
                                       (FERPA / COPPA / GDPR / DSGVO / LGPD) + a DATE
  D2+ DISCLOSURE-OF-SCOPE              D2, plus an explicit statement of what the piece does
                                       NOT touch (no accounts, no grades, public data only)
  D2  DISCLOSURE-OF-NON-AFFILIATION    unofficial / not affiliated with the NAMED provider
  D3  DISCLOSURE-OF-HANDLING-ONLY      says what it does with credential/data (local-only,
                                       read-only) and is SILENT on the contractual plane
  D4  NO-DISCLOSURE                    none of the above

The discipline this inherits from P171, and the reason the classifier is this fussy:
a declaration is a CLAIM WITH A SUBJECT, never a word appearing somewhere.  "read-only"
inside a feature list is not a disclosure of handling; "license" in a dependency name is not
a cession (P171); and a project saying it is "safe" is not saying it is unofficial.

D3 is the trap this instrument exists to catch.  A promise about handling ("your password
never leaves your machine") answers a question nobody asked and stays silent on the one the
client's legal review WILL ask.  It reads reassuring and classifies LOW, by design.
"""
import re
import sys

# Each probe is (name, compiled regex).  All are matched against the raw text, case-folded
# only where the term is not a proper noun.
_TOU_QUOTE = re.compile(
    r"(terms of (use|service)|acceptable use|\bToU\b|\bToS\b|terms and conditions)",
    re.I)
# The admission is the expensive part: the project says the PROVIDER may object.
_PROVIDER_RISK = re.compile(
    r"(may (be )?(treat|consider|regard|deem)\w*\b[^.]{0,60}\b(violation|breach|unauthori[sz]ed)"
    r"|at your own risk"
    r"|(violat\w+|breach\w*)\b[^.]{0,40}\b(terms|agreement)"
    r"|(may|could)\b[^.]{0,40}\b(suspend|terminate|revoke|ban)\b"
    r"|auf eigene Verantwortung"                  # DE: "use at your own risk"
    r"|por sua conta e risco)",
    re.I)
_STATUTE = re.compile(r"\b(FERPA|COPPA|GDPR|DSGVO|LGPD|HIPAA|AI Act)\b")
_DATE = re.compile(r"\b(20\d{2}-\d{2}-\d{2}|\d{2}/\d{2}/20\d{2}|\d{1,2} \w+ 20\d{2})\b")
_NON_AFFIL = re.compile(
    r"(unofficial"
    r"|n[aã]o[- ]oficial"
    r"|inoffiziell\w*|nicht offiziell"            # DE: the word is "inoffiziell"
    r"|keine Verbindung zu"                       # DE: "no connection to <provider>"
    r"|không chính thức"                        # VI
    r"|no (connection|affiliation)\b"
    r"|not (affiliated|endorsed|associated)\b"
    r"|sem v[ií]nculo\b"
    r"|community[- ]run)",
    re.I)
# Scope: the piece says what it does NOT reach.  Two shapes: "only public data", or an
# explicit no-list.
_SCOPE = re.compile(
    r"((only|exclusively)\b[^.]{0,40}\b(public|unauthenticated)\b"
    r"|\bno\b[^.]{0,40}\b(student accounts?|grades?|login[- ]protected|credentials?)\b"
    r"|does not (access|touch|read|require)\b[^.]{0,50}\b(account|grade|credential|password)\b"
    r"|never (touches|reads|accesses|sees)\b[^.]{0,80}\b(account|grade|schedule|login|record|password)\b"
    r"|everything it reads is public\b)",
    re.I)
_HANDLING = re.compile(
    r"(never leaves? (your|the) (computer|machine|device)"
    r"|n[aã]o vai para nenhum servidor"
    r"|stored? (only )?locally|processed? (entirely )?locally"
    r"|(read[- ]only|somente leitura|s[oó] l[eê])"
    r"|xu? l[yý] ho[aà]n to[aà]n tr[eên] m[aá]y c[uụ]c b[oộ]"
    r"|local[- ]only|local execution"
    r"|x[u\u1ef1] l[y\u00fd] c[u\u1ee5]c b[o\u1ed9]"          # VI: "processed locally"
    r"|kh[o\u00f4]ng l[u\u01b0]u tr[u\u1ef1] t[a\u1eadp] trung"  # VI: "no central storage"
    r"|lokal verarbeitet|bleibt lokal)",                  # DE
    re.I)


def classify(text: str) -> tuple[str, str, list[str]]:
    """-> (class, label, the probes that fired).  Pure: no IO, no network."""
    fired = []
    tou = bool(_TOU_QUOTE.search(text))
    risk = bool(_PROVIDER_RISK.search(text))
    statute = bool(_STATUTE.search(text))
    dated = bool(_DATE.search(text))
    non_affil = bool(_NON_AFFIL.search(text))
    scope = bool(_SCOPE.search(text))
    handling = bool(_HANDLING.search(text))
    for name, hit in (("tou", tou), ("provider-risk", risk), ("statute", statute),
                      ("dated", dated), ("non-affiliation", non_affil),
                      ("scope", scope), ("handling", handling)):
        if hit:
            fired.append(name)

    # D1 is conjunctive on purpose.  Naming FERPA in a feature list is not an expedient;
    # the expedient is the ToU plus the admission plus the statute.
    if tou and risk and statute:
        return "D1", "DISCLOSURE-WITH-STATUTE-AND-TOU", fired
    if non_affil and scope:
        return "D2+", "DISCLOSURE-OF-SCOPE", fired
    if non_affil:
        return "D2", "DISCLOSURE-OF-NON-AFFILIATION", fired
    if handling or scope:
        return "D3", "DISCLOSURE-OF-HANDLING-ONLY", fired
    return "D4", "NO-DISCLOSURE", fired


def main() -> int:
    slug = sys.argv[1] if len(sys.argv) > 1 else "-"
    text = sys.stdin.read()
    cls, label, fired = classify(text)
    print(f"{slug}\t{cls}\t{label}\t{','.join(fired) or '-'}\t{len(text)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
