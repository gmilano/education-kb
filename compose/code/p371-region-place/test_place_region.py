#!/usr/bin/env python3
"""`p371-region-place` controls.  Runnable from this directory (`p355-cwd-portability`:
every suite on this base must pass from inside its own folder, and the Makefile `cd`s in).

Each control names the string that prompted it.  Negative controls first, because the
ways this instrument can be WRONG cost more than the ways it can be right: a wrong
region does not read downstream as a guess.
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from place_region import place, place_both, serves  # noqa: E402

FAILED = []


def check(name, got, want):
    if got != want:
        FAILED.append(f"{name}\n      got  {got!r}\n      want {want!r}")


# ───────────────────────────── negative controls: what must NEVER place a row

def t_a_maintainer_name_never_moves_a_region():
    """`P800`'s own negative control, carried here verbatim in intent. Three rows whose
    maintainers carry placeable-looking names and whose payloads say nothing."""
    for slug, readme in [
        ("GhaithAlHallak8/moodler-mcp", "# moodler-mcp\nA Moodle MCP server."),
        ("Jawadh-Salih/moodle-mcp-server", "# moodle-mcp-server\nTools for Moodle."),
        ("TanimowoObaloluwaDavid/credential-lens", "# credential-lens\nVerify credentials."),
    ]:
        region, channel, _ = place(slug, readme)
        check(f"name-never-places[{slug}]", (region, channel), ("Global", "-"))


def t_a_language_never_places_a_row():
    """🔴 A Spanish README is not LATAM — Spain is EMEA. This base's own `P521` finding
    came from a Portuguese query that returned EMEA and LATAM trees in one result set."""
    readme = ("# Asistente educativo\nUn tutor inteligente para estudiantes. "
              "Instalación y configuración de la plataforma de aprendizaje.")
    check("language-never-places", place("someone/asistente", readme), ("Global", "-", "-"))


def t_a_badge_host_never_places_a_row():
    """`p115-D`, one field over: a badge block is the densest source of foreign-looking
    hosts in any README and none of them are geography."""
    readme = ("# tool\n![build](https://travis-ci.org/x/y.svg)\n"
              "[![cov](https://codecov.io/gh/x/y/badge.svg)](https://codecov.io/gh/x/y)\n"
              "![chat](https://discord.gg/abcd)  https://youtu.be/xyz\n")
    check("badge-never-places", place("x/y", readme), ("Global", "-", "-"))


def t_a_vanity_tld_never_places_a_row():
    """`p115`: `.io` is never placed even from a typed field, and `.ai`/`.co` are vanity
    rows in the committed table. A docs site on `.io` is not a country."""
    readme = "# platform\nDocs at https://docs.tutorkit.io and https://learn.tutorkit.ai"
    check("vanity-never-places", place("x/y", readme), ("Global", "-", "-"))


def t_a_slug_token_never_places_a_row():
    """`p370-domain-check`'s lesson, one field over: the slug is not the payload."""
    readme = "# tool\nNo institution, no standard, no host."
    check("slug-never-places", place("ministry-of-education-france/tool", readme),
          ("Global", "-", "-"))


def t_bare_dot_edu_PLACES_north_america_and_this_controls_premise_was_WRONG():
    """🔴 **D1 in this instrument's own first draft, and the defect was in the CONTROL,
    not the code.** This control first asserted that `example.edu` must NOT place, on the
    reasoning that Globant engages universities outside the US holding `.edu` names. 🟢
    `p115`'s committed table disagrees, with its reason in the row: `edu  cc  North
    America  registry policy: US-accredited postsecondary only`. **EDUCAUSE has restricted
    `.edu` to US-accredited postsecondary institutions since 2001, so the TLD carries a
    jurisdiction that `.com` does not.** The committed table was right; the control is
    inverted here to match it.

    🟡 The declared limit, which is the honest residue of the wrong assumption: a small
    set of non-US institutions hold pre-2001 `.edu` names, so this channel has a known
    false-positive class. It is channel **4**, the last resort, and `OWNER`, `STANDARD`
    and `INSTITUTION` all overrule it."""
    # 🟡 NOT `example.edu` — D3 reserves that name. A real-shaped `.edu` host.
    readme = "# course tools\nUsed at https://registrar.purdue.edu for CS1."
    region, channel, _ = place("x/y", readme)
    check("bare-.edu-places-NA", (region, channel), ("North America", "CCTLD"))


# ───────────────────────────── positive controls: the four channels

def t_owner_channel_places_from_the_committed_table():
    """`p115`'s `orgs.region.tsv` is a committed file; this reads it rather than a list
    inlined here, so the two can never drift."""
    check("owner[openedx]", place("openedx/XBlock", "")[:2], ("North America", "OWNER"))
    check("owner[opetushallitus]", place("opetushallitus/x", "")[:2], ("EMEA", "OWNER"))
    check("owner[CAHLR]", place("CAHLR/OATutor", "")[:2], ("North America", "OWNER"))


def t_owner_channel_folds_case():
    """`ACTION UH`: `OpenOLAT/OpenOLAT` and `openolat/OpenOLAT` are one row."""
    check("owner-case-folds", place("OPENEDX/frontend", "")[:2], ("North America", "OWNER"))


def t_a_regional_regulator_answers_SERVES_and_never_ORIGIN():
    """🔴 The split that `p115`'s stoplist header forced: *"a repository that CITES the
    EU AI Act is not a European repository."* 🟢 It is still worth knowing which regime
    it implements, so a regulator fills a `SERVES` cell and leaves `ORIGIN` empty."""
    for text, want in [("FERPA-compliant student records.", "North America"),
                       ("All data handling is GDPR compliant.", "EMEA"),
                       ("Conforme a LGPD e a BNCC.", "LATAM"),
                       ("Follows the DPDP Act for student data.", "APAC")]:
        check(f"serves[{want}]", serves(text)[0], want)
        check(f"regulator-does-not-place-origin[{want}]", place("x/y", text)[:2],
              ("Global", "-"))


def t_the_two_claims_are_reported_SIDE_BY_SIDE_never_merged():
    """A US-origin repository implementing GDPR is both facts at once, and collapsing
    them to one cell loses the one an engagement needs."""
    origin, channel, _, serves_region = place_both(
        "openedx/x", "GDPR compliant deployment for EU tenants.")
    check("both-origin", (origin, channel), ("North America", "OWNER"))
    check("both-serves", serves_region, "EMEA")


def t_institution_channel_places_through_the_committed_tld_table():
    check("inst[ac.uk]", place("x/y", "Deployed at www.cs.ox.ac.uk for teaching.")[:2],
          ("EMEA", "INSTITUTION"))
    check("inst[edu.au]", place("x/y", "In use at https://unimelb.edu.au.")[:2],
          ("APAC", "INSTITUTION"))
    check("inst[gob.mx]", place("x/y", "Datos de https://sep.gob.mx/datos.")[:2],
          ("LATAM", "INSTITUTION"))


def t_D2_a_host_with_no_URL_CONTEXT_never_places_a_row():
    """🔴 **D2, and it is this instrument's expensive defect.** Its first real run placed
    eight of `p370`'s 63 addresses in LATAM; five of those read `server.py`, `main.py`,
    `setup.py`, `database.py`, `api.py` in the evidence column. **`.py` is Paraguay in
    `p115`'s table, and a Python filename is not a hostname.** 🟢 `p115`'s own
    `tokens.awk` requires `https?://` or `//` before a host; that discipline is reused
    here rather than restated, and these are the exact strings that caused the defect."""
    for fname in ["server.py", "main.py", "setup.py", "database.py", "api.py",
                  "core-updates-watch.py", "index.sh", "run.pl", "notes.md"]:
        check(f"filename-never-places[{fname}]", place("x/y", f"Run `{fname}` to start."),
              ("Global", "-", "-"))


def t_D2_a_placeholder_config_host_still_needs_a_scheme():
    """`d2l.myschool.edu` came out of a placeholder configuration line on the first run
    and placed a row in North America. With no scheme it places nothing."""
    check("placeholder-host", place("x/y", "set BASE_URL=d2l.myschool.edu"),
          ("Global", "-", "-"))


def t_D3_an_RFC2606_placeholder_host_never_places_a_row():
    """🔴 **D3, same first run.** `student.example.edu` placed a row in North America and
    `d2l.myschool.edu` placed another — both out of configuration SAMPLES. RFC 2606
    reserves the `example.*` names for documentation; a README's config block is
    documentation. The `myschool` family has no RFC and the same meaning."""
    for host in ["https://student.example.edu", "https://d2l.myschool.edu",
                 "https://example.com/docs", "https://lms.yourschool.edu",
                 "https://canvas.university.edu", "http://localhost:8000",
                 "https://demo.test",
                 # 🔴 D4's own string: hyphenated, and the first draft missed it
                 "https://blackboard.your-university.edu",
                 "https://moodle.your-school.edu.au", "https://lms.acme.com.br"]:
        check(f"placeholder-never-places[{host[:34]}]",
              place("x/y", f"Set BASE_URL={host}"), ("Global", "-", "-"))


def t_D3_a_real_institutional_host_still_places_after_the_placeholder_rule():
    """🟢 The negative control for D3's fix: the rule must not eat real universities.
    These are the exact hosts the fixed run placed on `p370`'s population."""
    for host, want in [("https://canvas.ox.ac.uk", "EMEA"),
                       ("https://i.nccu.edu.tw", "APAC"),
                       ("https://tup.sied.utn.edu.ar", "LATAM"),
                       ("https://www.icpsr.umich.edu", "North America"),
                       ("https://data-nsr.udir.no", "EMEA")]:
        check(f"real-host-still-places[{host[:30]}]", place("x/y", f"See {host}")[0], want)


def t_D4_the_placeholder_rule_reads_the_REGISTRABLE_label_only():
    """🔴 **D4.** The first draft of D3's fix matched any label, which would have thrown
    away `mycourses.rit.edu` — a real host at a real university whose geography sits in
    `rit`. 🟢 A `my…`/`your…` SUBDOMAIN of a real institution still places the row."""
    for host, want in [("https://mycourses.rit.edu", "North America"),
                       ("https://myuni.sydney.edu.au", "APAC"),
                       ("https://campus.unam.mx", "LATAM"),
                       ("https://student.tudelft.nl", "EMEA")]:
        check(f"registrable-label[{host[:32]}]", place("x/y", f"See {host}")[0], want)


def t_D5_a_link_shortener_never_places_a_row():
    """🔴 **D5, found on the 1 859-address run.** `rasbt/LLMs-from-scratch` placed in
    LATAM on `mng.bz/orYv` — **Manning's link shortener**, and `.bz` is Belize in
    `p115`'s table. 🟢 Exactly `p115-D`'s class (`bit.ly` is not Libyan), with the list
    extended to the shorteners this corpus actually contains."""
    for url in ["https://mng.bz/orYv", "https://rb.gy/abc", "https://cutt.ly/xyz",
                "https://t.ly/abc", "https://amzn.to/3xyz", "https://is.gd/abc",
                "https://tinyurl.com/abc", "https://forms.gle/abc"]:
        check(f"shortener-never-places[{url[:28]}]",
              place("x/y", f"Buy the book at {url}"), ("Global", "-", "-"))


def t_p115s_committed_stoplist_is_APPLIED_not_restated():
    """`p115-E`: a regulator, registry or standards host is not evidence of origin.
    🔵 The list is read from `p115`'s committed file, so the two cannot drift."""
    for host, why in [("https://ec.europa.eu/info", "EU institutions"),
                      ("https://eur-lex.europa.eu/eli/reg/2026/1744", "EU law portal"),
                      ("https://www.unesco.org/en/report", "intergovernmental"),
                      ("https://github.com/x/y", "forge"),
                      ("https://adlnet.gov/profiles", "xAPI steward, ADDED at p371"),
                      ("https://www.imsproject.org/spec", "1EdTech legacy, ADDED p371")]:
        check(f"stoplist[{why}]", place("x/y", f"See {host} for detail.")[:2],
              ("Global", "-"))


def t_cctld_channel_is_the_last_resort_and_still_only_cc_rows():
    check("cctld[.br]", place("x/y", "Veja https://escola.com.br/docs")[:2],
          ("LATAM", "CCTLD"))
    check("cctld[.jp]", place("x/y", "See https://manabi.co.jp/manual")[:2],
          ("APAC", "CCTLD"))


# ───────────────────────────── the conflict rule

def t_two_regions_at_one_precedence_is_a_SPLIT_not_a_coin_flip():
    """🔵 Silently taking the first match is how a filter stops working. A row that is
    two things at once is `Global` and SAYS which two."""
    region, ev = serves("Both FERPA and GDPR compliant.")
    check("serves-split-region", region, "Global")
    check("serves-split-names-both",
          ("EMEA" in ev and "North America" in ev and ev.startswith("SPLIT")), True)
    origin, channel, oev, _ = place_both(
        "x/y", "Hosted at https://www.ox.ac.uk and https://www.unimelb.edu.au.")
    check("origin-split-region", origin, "Global")
    check("origin-split-channel", channel, "SPLIT")
    check("origin-split-names-both", ("EMEA" in oev and "APAC" in oev), True)


def t_precedence_owner_beats_a_conflicting_host():
    """A committed institutional owner is stronger evidence than a host in prose."""
    check("precedence", place("openedx/x", "Mirror at https://www.ox.ac.uk/x")[:2],
          ("North America", "OWNER"))


def t_an_empty_payload_is_Global_and_not_an_error():
    """`P541`: an instrument must refuse to invent. An absent README is `Global`."""
    check("empty-payload", place("nobody/nothing", ""), ("Global", "-", "-"))
    check("none-payload", place("nobody/nothing", None), ("Global", "-", "-"))


def t_the_region_vocabulary_is_closed():
    """🔴 `region` is a CLOSED field — five values. Each variant becomes its own bucket
    and the filter stops working. This asserts the instrument cannot emit a sixth."""
    allowed = {"North America", "EMEA", "APAC", "LATAM", "Global"}
    samples = ["FERPA", "GDPR", "LGPD", "DPDP", "https://x.ac.uk", "https://x.edu.au",
               "", "Erasmus", "BNCC", "NCERT", "https://sep.gob.mx", "https://x.com.br",
               "server.py", "nothing at all"]
    for sample in samples:
        origin, _, _, serves_region = place_both("x/y", sample)
        check(f"closed-origin[{sample[:16]}]", origin in allowed, True)
        check(f"closed-serves[{sample[:16]}]", serves_region in allowed, True)


def main():
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("t_") and callable(v)]
    for t in tests:
        t()
    total = len(tests)
    if FAILED:
        print(f"🔴 FAIL — {len(FAILED)} control(s) of {total}:")
        for f in FAILED:
            print(f"  - {f}")
        return 1
    print(f"🟢 PASS — {total}/{total} controls, p371-region-place")
    return 0


if __name__ == "__main__":
    sys.exit(main())
