#!/usr/bin/env python3
"""`p371-region-place` — place a graded address in a region from its OWN payload.

🟢 WHY THIS EXISTS. The scheduled brief this base answers says it in one line: *"A finding
with no region attached is worth less than one that is placed."*  `p370` graded 63
addresses and placed none of them, because the probe captured a README and nothing read it
for geography.  The READMEs are already on disk; this reads them.

🔴 THE RULE IS `P800`'s AND IT IS NOT RELAXED HERE: **a region comes from an institution or
a standard the artefact NAMES, never from a person's name.**  `region` is a closed field
this KB filters on, so a guess does not read downstream as a guess — it reads as data.
`Global` is the honest value for an unplaced row and it costs nothing.

CHANNELS, in precedence order.  The first that answers places the row:

  1. OWNER       — `p115`'s committed `orgs.region.tsv`.  An owner that IS a national
                   agency, a university or a known vendor places the row outright.
  2. STANDARD    — a REGIONAL regulatory or standards instrument named in the payload:
                   FERPA/COPPA (North America), GDPR/AI Act/Erasmus (EMEA), DPDP (APAC),
                   LGPD/BNCC/SAEB/ENEM (LATAM).  These are jurisdictional by construction.
  3. INSTITUTION — an academic or government host in the payload, placed through `p115`'s
                   committed `country.region.tsv`: `.ac.uk`, `.edu.au`, `.gob.mx`, `.go.jp`.
                   🟡 A bare `.edu` host places North America on channel 4:
                   `p115`'s committed table carries `edu` as a `cc` row with
                   its reason in the row — *"registry policy: US-accredited
                   postsecondary only"*.
  4. CCTLD       — any other country-code host in the payload, `cc` class only.
                   🔴 `vanity` and `cc?` rows NEVER place, which is `p115`'s own finding:
                   `youtu.be` is not Belgian and `shields.io` is not in the Indian Ocean.

🔴 D1, THIS INSTRUMENT'S FIRST DEFECT, and it sat in the CONTROL rather than the
code: the suite asserted that a bare `.edu` host must NOT place a row, reasoning
that Globant engages universities outside the US holding `.edu` names. 🟢 `.edu`
has been restricted to US-accredited postsecondary institutions since 2001, which
is why `p115` committed it as `cc`. The control is inverted to match the table, and
the residual false-positive class — pre-2001 non-US `.edu` holders — is declared
here rather than smoothed. It is the LAST channel; `OWNER`, `STANDARD` and
`INSTITUTION` all overrule it.

🔴 FOUR THINGS THAT NEVER PLACE A ROW, each because it produced a wrong answer somewhere:
  - a personal name (`P800`'s negative control, kept as this suite's too)
  - a language (a Spanish README is not LATAM: Spain is EMEA, and this base's own
    `P521` finding came from a PORTUGUESE query returning EMEA and LATAM trees alike)
  - a badge, shield or CI host (`p115-D`)
  - a slug token (`p370-domain-check`'s whole lesson, one field over)

CONFLICT: two channels at the same precedence disagreeing is reported as `SPLIT` and
placed `Global`.  🔵 A split is a measurement, not a failure, and silently taking the
first one is how a filter stops working.

No network: the caller supplies payload text.
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
P115 = os.path.join(HERE, os.pardir, "p115-region-evidence")

REGIONS = ("North America", "EMEA", "APAC", "LATAM", "Global")

# ---------------------------------------------------------------- channel 2: standards
# A regional instrument places a row because it only exists in one jurisdiction.
STANDARDS = [
    (r"\bFERPA\b", "North America"), (r"\bCOPPA\b", "North America"),
    (r"\bIDEA\s+Part\s+B\b", "North America"), (r"\bOneRoster\b.{0,40}\bstate\b", "North America"),
    (r"\bEd-?Fi\b", "North America"), (r"\bESSA\b", "North America"),
    (r"\bGDPR\b", "EMEA"), (r"\bEU\s+AI\s+Act\b", "EMEA"), (r"\bAI\s+Act\b", "EMEA"),
    (r"\bErasmus\b", "EMEA"), (r"\bBologna\s+Process\b", "EMEA"),
    (r"\bEuropean\s+Learner\s+Model\b", "EMEA"), (r"\bEuropass\b", "EMEA"),
    (r"\bDPDP\b", "APAC"), (r"\bNEP\s*2020\b", "APAC"), (r"\bCBSE\b", "APAC"),
    (r"\bNCERT\b", "APAC"), (r"\bGaokao\b", "APAC"),
    (r"\bLGPD\b", "LATAM"), (r"\bBNCC\b", "LATAM"), (r"\bSAEB\b", "LATAM"),
    (r"\bENEM\b", "LATAM"), (r"\bSARESP\b", "LATAM"), (r"\bSEP\b.{0,30}\bM[eé]xico\b", "LATAM"),
]

# ───────────────────────────── host extraction: a URL CONTEXT is required
#
# 🔴 D2, AND IT IS THE EXPENSIVE ONE. This instrument's first real run placed EIGHT of
# `p370`'s 63 addresses in LATAM, and the evidence column for five of them read
# `server.py`, `main.py`, `setup.py`, `database.py`, `api.py`. **`.py` is Paraguay in
# `p115`'s country table, and a Python filename is not a hostname.** Also caught:
# `d2l.myschool.edu` out of a placeholder config line.
#
# 🟢 `p115` ALREADY KNEW. Its `tokens.awk` extracts a host only after `https?://` or
# `//`, and it ships a committed `stoplist.tsv` whose header states the rule this
# instrument had to rediscover: *"A HOSTNAME WHOSE TLD IS A REAL COUNTRY CODE IS STILL
# NOT EVIDENCE WHEN THE HOST IS A SERVICE, A REGISTRY, A STANDARDS BODY OR A
# REGULATOR."* 🔵 Same shape as `p369` paying to rediscover `LICENSE.TXT` that
# `p189` had already recorded: the knowledge was committed and was not wired into the
# next instrument that needed it. Both disciplines are now reused here, not restated.
URLISH = re.compile(r"(?:https?://|//|\bwww\.|[A-Za-z0-9._%+-]+@)"
                    r"([A-Za-z0-9][A-Za-z0-9.-]*\.[A-Za-z]{2,24})")

# a second-level academic/government label under a country code, inside a real host
INSTITUTION_SUFFIX = re.compile(
    r"\.(?:ac|edu|sch|gov|gob|gouv|go|govt|org)\.([a-z]{2})$", re.I)


def load_stoplist():
    """`p115`'s committed service/standards/regulator hosts, matched as a DOMAIN SUFFIX
    on a label boundary — `europa.eu` matches `ec.europa.eu`, never `noteuropa.eu`."""
    out = []
    path = os.path.join(P115, "stoplist.tsv")
    try:
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                if line.startswith("#") or not line.strip():
                    continue
                out.append(line.split("\t")[0].strip().lower())
    except FileNotFoundError:
        return []
    return [s for s in out if s]


STOPLIST = load_stoplist()


def stopped(host):
    host = host.lower().rstrip(".")
    for suffix in STOPLIST:
        if host == suffix or host.endswith("." + suffix):
            return suffix
    return None


# 🔴 D3, found on the same first run: `student.example.edu` placed a row in North
# America and `d2l.myschool.edu` placed another. **RFC 2606 reserves `example.com`,
# `example.net`, `example.org` and the `.example`/`.invalid`/`.test`/`.localhost` names
# for documentation**, and a README's configuration sample is documentation by
# definition. The `myschool`/`your-university` family has no RFC and the same meaning.
#
# 🔴 D4, found while fixing D3: the first draft matched the placeholder word against
# ANY label, which both missed `blackboard.your-university.edu` (the word is
# `your-university`, hyphenated) and would have WRONGLY rejected `mycourses.rit.edu` —
# a real host at a real university, whose geography sits in `rit`, not in `mycourses`.
# 🟢 The test therefore runs on the REGISTRABLE LABEL only: the label immediately left
# of the public suffix. That is the one an institution registers and the only one that
# carries geography.
PLACEHOLDER_WORD = re.compile(
    r"^(?:(?:my|your|our|some|any)[-_]?[a-z0-9]*"
    r"|example|school|university|college|institution|district|campus|tenant|client"
    r"|test|testing|localhost|invalid|sample|demo|placeholder|changeme|dummy"
    r"|foo|bar|baz|acme|contoso|fabrikam|lorem|xxx|abc|domain|subdomain|host"
    r"|hostname|server|yourdomain|mydomain)$", re.I)
PLACEHOLDER_TLD = re.compile(r"\.(?:example|invalid|test|localhost|local)$", re.I)

# Public suffixes that take TWO labels, so the registrable label is the third from the
# right.  Only the ones this corpus actually produces — an incomplete list that is
# CORRECT on what it covers beats a guess that silently mis-splits a real host.
TWO_LABEL_SUFFIX = re.compile(
    r"\.(?:ac|edu|sch|gov|gob|gouv|go|govt|net|or|ne|co|com|org|mil|info|k12|res|nic)"
    r"\.[a-z]{2}$", re.I)


def registrable_label(host):
    """-> the label that carries the geography, or None if the host has no such label."""
    host = host.lower().rstrip(".")
    if "." not in host:
        return host or None
    stem = TWO_LABEL_SUFFIX.sub("", host)
    if stem == host:                      # single-label suffix: drop just the TLD
        stem = host.rsplit(".", 1)[0]
    parts = [x for x in stem.split(".") if x]
    return parts[-1] if parts else None


def placeholder(host):
    """🟢 Documentation, not deployment. Tested on the registrable label only (D4)."""
    host = host.lower().rstrip(".")
    if PLACEHOLDER_TLD.search(host) or host in ("localhost",):
        return True
    label = registrable_label(host)
    return bool(label and PLACEHOLDER_WORD.match(label))


def hosts(text):
    """-> [host] in URL context, with `p115`'s stoplist applied."""
    out = []
    for m in URLISH.finditer(text or ""):
        host = m.group(1).lower().rstrip(".")
        if INFRA.search(host) or stopped(host) or placeholder(host):
            continue
        out.append(host)
    return out

# `p115-D`: a badge or CI host is infrastructure, never geography.
INFRA = re.compile(
    r"shields\.io|badge|travis-ci|circleci|codecov|coveralls|appveyor|snyk\.io|"
    r"gitpod\.io|readthedocs|netlify\.app|vercel\.app|herokuapp|githubusercontent|"
    r"github\.io|gitlab\.io|sourceforge|npmjs|pypi|packagist|docker|gravatar|"
    r"youtu\.be|bit\.ly|goo\.gl|t\.me|discord\.gg|linkedin|twitter|x\.com|"
    # 🔴 D5, found on the 1 859-address run: `rasbt/LLMs-from-scratch` placed in LATAM
    # on `mng.bz/orYv` — **Manning's link shortener**, and `.bz` is Belize. This is
    # `p115-D`'s own class (`bit.ly` is not Libyan) with the list extended to the
    # shorteners this corpus actually contains.
    r"mng\.bz|tinyurl|rb\.gy|cutt\.ly|buff\.ly|ow\.ly|is\.gd|amzn\.to|dub\.sh|"
    r"t\.ly|lnkd\.in|forms\.gle|shorturl|tiny\.cc|rebrand\.ly|short\.io|smarturl",
    re.I)


def load_orgs():
    out = {}
    path = os.path.join(P115, "orgs.region.tsv")
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 2:
                continue
            owner, region = parts[0].strip(), parts[1].strip()
            if region in REGIONS:
                out[owner.lower()] = region
    return out


def load_tlds():
    """-> {tld: (class, region)}.  Only `cc` rows can place; everything else is recorded
    so a caller can SAY why a row was not placed."""
    out = {}
    path = os.path.join(P115, "country.region.tsv")
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            tld, klass, region = parts[0].strip().lower(), parts[1].strip(), parts[2].strip()
            out[tld] = (klass, region if region in REGIONS else None)
    return out


ORGS = load_orgs()
TLDS = load_tlds()


def _cc_region(tld):
    """A region ONLY from a `cc` row. `vanity`, `cc?`, `gtld` never place."""
    klass, region = TLDS.get(tld.lower(), (None, None))
    return region if klass == "cc" and region else None


def place(slug, payload):
    """-> (region, channel, evidence) — the ORIGIN/DEPLOYMENT reading, kept for the
    callers and controls that want one value. `Global` with channel `-` means unplaced.

    🔵 Prefer `place_both()`: it returns the jurisdictional reading alongside, and the
    two are different claims about a repository."""
    region, channel, ev, _ = place_both(slug, payload)
    return region, channel, ev


def serves(payload):
    """-> (region, evidence) — the JURISDICTION the artefact's own text binds it to.

    🔴 THIS IS A DIFFERENT CLAIM FROM ORIGIN AND IS NOT ALLOWED TO BECOME ONE. `p115`'s
    stoplist header makes the point in the opposite direction: *"a repository that CITES
    the EU AI Act is not a European repository"*. 🟢 True, and it is still worth knowing
    that a repository implements FERPA rather than LGPD, because that is the question an
    engagement asks in week one. So the regional regulator places a `SERVES` cell and
    never an `ORIGIN` cell, and the shelves carry the two separately.

    🟡 `p359`'s limit, restated for this channel: subject matter is strong corroboration
    and weak attribution. This base already places `mcp-brasil` LATAM on its subject
    matter and says so.
    """
    text = payload or ""
    clean = "\n".join(l for l in text.splitlines() if not INFRA.search(l))
    found = {}
    for pat, region in STANDARDS:
        m = re.search(pat, clean, re.I)
        if m:
            found.setdefault(region, m.group(0).strip())
    if len(found) == 1:
        region, ev = next(iter(found.items()))
        return region, ev
    if len(found) > 1:
        return "Global", "SPLIT:" + "+".join(sorted(found))
    return "Global", "-"


def place_both(slug, payload):
    """-> (origin_region, origin_channel, origin_evidence, serves_region).

    Origin precedence: OWNER (a committed institutional owner) > INSTITUTION (an
    academic or government host) > CCTLD (any other country host). Every host must
    appear in a URL context and survive `p115`'s stoplist — see D2.
    """
    owner = slug.split("/")[0] if "/" in slug else slug
    text = payload or ""
    serves_region, _ = serves(text)

    # 1. owner — the strongest channel, and a committed file rather than a judgement
    hit = ORGS.get(owner.lower())
    if hit:
        return hit, "OWNER", owner, serves_region

    clean = "\n".join(l for l in text.splitlines() if not INFRA.search(l))
    host_list = hosts(clean)

    # 2. institution — an academic or government second-level label under a country code
    inst = {}
    for host in host_list:
        m = INSTITUTION_SUFFIX.search(host)
        if not m:
            continue
        region = _cc_region(m.group(1))
        if region:
            inst.setdefault(region, host)
    if len(inst) == 1:
        region, ev = next(iter(inst.items()))
        return region, "INSTITUTION", ev, serves_region
    if len(inst) > 1:
        return "Global", "SPLIT", "+".join(sorted(inst)), serves_region

    # 3. any other country host
    cc = {}
    for host in host_list:
        tld = host.rsplit(".", 1)[-1]
        region = _cc_region(tld)
        if region:
            cc.setdefault(region, host)
    if len(cc) == 1:
        region, ev = next(iter(cc.items()))
        return region, "CCTLD", ev, serves_region
    if len(cc) > 1:
        return "Global", "SPLIT", "+".join(sorted(cc)), serves_region

    return "Global", "-", "-", serves_region


def main(argv):
    if len(argv) < 2:
        sys.stderr.write("place_region.py <tree-run.tsv> <trees-dir> — refusing (P541)\n")
        return 2
    run, outdir = argv[0], argv[1]
    print("\t".join(["slug", "origin_region", "origin_channel",
                     "origin_evidence", "serves_region", "serves_evidence"]))
    with open(run, encoding="utf-8") as fh:
        header = fh.readline().rstrip("\n").split("\t")
        for line in fh:
            if not line.strip():
                continue
            r = dict(zip(header, line.rstrip("\n").split("\t")))
            slug = r.get("slug", "")
            if not slug:
                continue
            key = slug.replace("/", "%")
            path = os.path.join(outdir, key + ".readme")
            payload = ""
            if os.path.exists(path):
                with open(path, encoding="utf-8", errors="replace") as rf:
                    payload = rf.read()
            region, channel, ev, serves_region = place_both(slug, payload)
            _, serves_ev = serves(payload)
            print("\t".join([slug, region, channel, ev.replace("\t", " ")[:80],
                             serves_region, serves_ev.replace("\t", " ")[:40]]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
