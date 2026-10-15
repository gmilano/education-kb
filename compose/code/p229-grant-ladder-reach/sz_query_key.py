"""`ACTION SZ` — key the inbound gate on the `(query, record)` PAIR, not the record's text.

p228's `ACTION SP` tried to narrow the EU AI Act subject by requiring a jurisdiction token
in the RECORD, and fired limb `2` (STOP): the narrowing dropped a genuine EU record — EU by
the question that produced it, jurisdiction-free in its own words — while gaining an
irrelevant one. `SZ` is the registered successor: change the KEY, not the pattern.

A search record does not arrive alone. It arrives as the answer to a QUERY, and the query
carries the jurisdiction the record inherits. `ACTION RE` has required the verbatim query
beside every finding for ten passes, so the pair is already on disk — this instrument just
stops throwing half of it away.

Offline, on p228's own `sp-subject-narrowing` records, exactly as the falsifier prescribes.
"""
import re
import sys

EU_QUERY = re.compile(r'(?i)\b(emea|europe|european|eu)\b|\b(germany|france|spain|italy|'
                      r'sweden|netherlands|poland|ireland|portugal|belgium|austria|denmark|'
                      r'finland|norway|greece|czech|hungary|romania)\b')
NON_EU_QUERY = re.compile(r'(?i)\b(vietnam|viet nam|apac|asia|korea|japan|china|india|'
                          r'singapore|taiwan|indonesia|latam|latin america|brazil|mexico|'
                          r'chile|colombia|africa|kenya|nigeria|north america|usa|united states|canada)\b')


def jurisdiction_of_query(query):
    """EU / NON-EU / UNSCOPED. A query naming BOTH is NON-EU: the narrower wins, because a
    record answering 'EU and Vietnam' is about Vietnam as often as not."""
    if NON_EU_QUERY.search(query or ''):
        return 'NON-EU'
    if EU_QUERY.search(query or ''):
        return 'EU'
    return 'UNSCOPED'


def gate(query, record, subject_re):
    """Fire only when the SUBJECT matches the record AND the QUERY is EU-scoped.

    An UNSCOPED query falls back to the record's own text, which is p228's `NEW` pattern —
    so `SZ` never sees LESS than `SP` did; it only re-admits what the pair can vouch for.
    """
    if not re.search(subject_re, record or ''):
        return (False, 'SUBJECT-ABSENT')
    j = jurisdiction_of_query(query)
    if j == 'EU':
        return (True, 'EU-BY-QUERY')
    if j == 'NON-EU':
        return (False, 'DROPPED-BY-QUERY-JURISDICTION')
    return (bool(re.search(r'(?i)(\bai act\b|annex\s+iii|reg\.?\s*\(eu\))', record)),
            'UNSCOPED-FALLS-BACK-TO-RECORD')


SUBJECT = r"(?i)(ai act|annex iii|anexo iii|alto riesgo|high-risk)"

CONTROLS = [
    ('AI education EMEA 2026 adoption regulation players',
     'Education tools that evaluate learners or influence access to qualifications fall '
     'into the high-risk category', True,
     "the genuine EU record SP DROPPED: EU by its query, jurisdiction-free in its text"),
    ('Vietnam Decision 33/2026/QD-TTg high-risk AI education',
     'AI systems that use AI to automatically test, evaluate results, and rank learners '
     'are classified high-risk', False, 'Vietnamese record, Vietnamese query -> dropped'),
    ('AI education APAC 2026 adoption regulation players',
     'A July 2026 decision lists education, including automated assessment, as high-risk',
     False, 'APAC query -> dropped even though the text is jurisdiction-free'),
    # 🔴 This control's FIRST draft truncated the record at `27 July 2026` and asserted it
    # must fire. It did not — and the CONTROL was the thing that was wrong: the subject
    # token (`AI Act`) sits in the clause the truncation cut off. Recorded rather than
    # quietly lengthened, because it is `ACTION RE`'s rule one layer down: a record stored
    # without its full text cannot be re-tested, and a control built on a truncation tests
    # the truncation and not the gate.
    ('AI education EMEA 2026 adoption regulation players',
     'One Commission page lists the AI Omnibus amendments as entering force on 27 July '
     '2026, with the AI Act itself entering force on 3',
     True, 'EU record SP also kept -> no regression'),
    ('open source AI agents education github MIT',
     'a vendor blog mentions the AI Act in passing', True,
     'UNSCOPED query falls back to the record, which names the AI Act'),
    ('open source AI agents education github MIT',
     'a high-risk deployment of a grading model', False,
     'UNSCOPED + no EU token in the record -> stays dropped, exactly as SP wanted'),
]


def main():
    bad = 0
    for q, r, expect, why in CONTROLS:
        got, reason = gate(q, r, SUBJECT)
        ok = got == expect
        bad += 0 if ok else 1
        print('%s fires=%-5s expect=%-5s %-32s %s' % ('ok ' if ok else 'FAIL', got, expect, reason, why))
    print('\n%d/%d controls pass' % (len(CONTROLS) - bad, len(CONTROLS)))
    return bad


if __name__ == '__main__':
    sys.exit(1 if main() else 0)
