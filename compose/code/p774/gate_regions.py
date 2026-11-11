#!/usr/bin/env python3
"""p774 gate-regions -- written FROM SCRATCH for ACTION p773-A.

`make hooks` was tried as the first command of p774 and DENIED a FIFTH
consecutive session (`[Code from External]`). No gate script was copied out of
the repository to evade that denial; this file implements, independently, the
ONE contract ACTION p773-A names:

  the region vocabulary is CLOSED to five values -- North America, EMEA, APAC,
  LATAM, Global -- both in every file's YAML frontmatter and in every `###`
  directly under `## Opportunities by region`.

Why this gate and not another: a variant spelling does not fail loudly. It
silently creates a SECOND bucket, so the region filter keeps working and
quietly returns less. That is the failure mode the ingest brief calls out by
name, and it is mechanically checkable without any repository code.

Contracts
  R1  a shelf has YAML frontmatter, opened by `---` on line 1 and closed
  R2  frontmatter `region:` holds exactly ONE value, and it is in the vocabulary
  R3  every `###` in the block under `## Opportunities by region` is a vocabulary value
  R4  a file carries at most ONE `## Opportunities by region`, spelled exactly
  R5  no near-miss variant ("Latam", "Europe", "Brazil", "APAC region", ...)
      is used WHERE A REGION VALUE IS EXPECTED

Instrument defences (each of these is a defect this gate had, or would have
had, and the control that holds it down):
  C-fence   a `##` inside a ``` fence is not a heading           -> K5
  C-scope   a `### North America` outside the Opportunities block is prose,
            not a region declaration, and must not be flagged    -> K7
  C-depth   `####` is not `###`                                  -> K10
  C-quote   `region: "LATAM"` is the same value as `region: LATAM`-> K9
  C-menu    the brief's template line is a MENU of five choices; a file that
            ships it verbatim has published the example as data   -> K8
"""
import re, sys, os

VOCAB = ["North America", "EMEA", "APAC", "LATAM", "Global"]
VOCAB_CI = {v.lower(): v for v in VOCAB}
OPP = "## Opportunities by region"

# C-menu: the exact template line from the ingest brief, in any order/spacing.
def is_menu(raw):
    parts = [p.strip() for p in raw.split("|")]
    return len(parts) > 1 and sum(1 for p in parts if p.lower() in VOCAB_CI) >= 2

# C-quote: strip quotes/backticks/trailing comment, keep the value itself.
def clean(raw):
    s = raw.strip()
    s = re.sub(r"\s+#.*$", "", s)
    s = s.strip().strip('"').strip("'").strip("`").strip()
    return s

# R5: variants that mean a region but are not the vocabulary spelling.
VARIANTS = [
    r"lat\.?am", r"latin\s*america", r"america\s*latina", r"south\s*america",
    r"europe", r"emea\s+region", r"eu\b", r"asia[\s\-]*pacific", r"apac\s+region",
    r"north[\s\-]america(?!$)", r"n\.?\s*america", r"usa?\b", r"united\s*states",
    r"brazil", r"brasil", r"mexico", r"argentina", r"chile", r"colombia",
    r"uk\b", r"england", r"germany", r"india", r"china", r"japan", r"worldwide",
    r"all\s*regions", r"global\s+\w+",
]
def variant_hit(s):
    low = s.lower()
    for v in VARIANTS:
        if re.fullmatch(v, low) or re.fullmatch(v + r"[\s,/&\-].*", low):
            return v
    return None

def strip_decoration(h):
    """Heading text minus emoji/bold/backticks, for reporting AND for the
    permissive read. Deliberately does NOT strip trailing ' -- blurb': a
    region heading must be the region, not the region plus commentary."""
    s = re.sub(r"[\U0001F300-\U0001FAFF☀-➿️]", "", h)
    s = s.replace("**", "").replace("`", "").strip()
    return s.strip()

def scan(path, text):
    """Return a list of (contract, line, detail). Fence-aware, scope-aware."""
    out = []
    lines = text.split("\n")

    # ---- R1/R2: frontmatter --------------------------------------------
    if not lines or lines[0].strip() != "---":
        out.append(("R1", 1, "no frontmatter: line 1 is not '---'"))
    else:
        end = None
        for i in range(1, min(len(lines), 40)):
            if lines[i].strip() == "---":
                end = i
                break
        if end is None:
            out.append(("R1", 1, "frontmatter opened but not closed within 40 lines"))
        else:
            fm = lines[1:end]
            regions = [(i + 2, l) for i, l in enumerate(fm)
                       if re.match(r"\s*region\s*:", l)]
            if not regions:
                out.append(("R2", 1, "frontmatter has no region: key"))
            for ln, l in regions:
                raw = clean(l.split(":", 1)[1])
                if is_menu(raw):
                    out.append(("R2", ln,
                                "MENU PUBLISHED AS DATA: region holds the brief's "
                                f"five-choice template line, not a choice: {raw!r}"))
                elif raw.lower() not in VOCAB_CI:
                    v = variant_hit(raw)
                    out.append(("R5" if v else "R2", ln,
                                f"region {raw!r} is not in the closed vocabulary"
                                + (f" (variant of /{v}/)" if v else "")))
                elif VOCAB_CI[raw.lower()] != raw:
                    out.append(("R2", ln,
                                f"region {raw!r} differs in case from "
                                f"{VOCAB_CI[raw.lower()]!r} -- a second bucket"))

    # ---- fence map ------------------------------------------------------
    infence = [False] * len(lines)
    f = False
    for i, l in enumerate(lines):
        if re.match(r"\s*(```|~~~)", l):
            f = not f
            infence[i] = True      # C-fence: the fence line itself is not a heading
            continue
        infence[i] = f

    # ---- R3/R4: the Opportunities block ---------------------------------
    opp_lines = [i for i, l in enumerate(lines)
                 if not infence[i] and l.strip().startswith("## ")
                 and strip_decoration(l.strip()[3:]).rstrip(" :") == "Opportunities by region"]
    # D2 (p774, this gate's own): a NARRATIVE pass heading that merely contains the
    # words "opportunities" and "region" is not an opportunities-by-region heading.
    # The first write matched any `##`/`###` holding both words and indicted 11 of
    # this base's own pass headings in archive/.
    # D3 (p774, this gate's own): `### (historical) Opportunities by region --
    # superseded, retained for history` is a DELIBERATE history marker at ### level,
    # not a qualified canonical heading. Only `##` is the canonical level.
    allopp = [i for i, l in enumerate(lines)
              if not infence[i] and re.match(r"\s*##\s", l)
              and re.match(r"opportunities\s+by\s+region\b",
                           strip_decoration(l.strip().lstrip("#").strip()), re.I)]
    # D4 (p774, this gate's own, and the one that mattered): a QUALIFIED heading --
    # `## Opportunities by region - p769` -- is this base's own supersession
    # convention, and it is the CORRECT way to retire a block without rewriting
    # append-only history. The first write of R4 called it a defect and would have
    # ordered 2 correct headings rewritten. The contract is ONE BARE heading per
    # file; a qualified one is history and is left alone.
    if len(opp_lines) > 1:
        out.append(("R4", opp_lines[1] + 1,
                    f"{len(opp_lines)} BARE '{OPP}' headings in one file. The live block "
                    "is one; a superseded block must be qualified with its pass "
                    "(this base's own convention) rather than left bare"))

    for start in opp_lines:
        seen = []
        for j in range(start + 1, len(lines)):
            l = lines[j]
            if infence[j]:
                continue
            if re.match(r"\s*#{1,2}\s", l):          # next ## or # closes the block
                break
            m = re.match(r"\s*###\s+(.*)$", l)       # C-depth: exactly three
            if not m:
                continue
            h = strip_decoration(m.group(1)).rstrip(" :")
            h = re.sub(r"\s*[-–—]{1,2}\s.*$", "", h).strip()
            if h.lower() in VOCAB_CI:
                if VOCAB_CI[h.lower()] != h:
                    out.append(("R3", j + 1, f"### {h!r} differs in case from "
                                             f"{VOCAB_CI[h.lower()]!r}"))
                seen.append(VOCAB_CI[h.lower()])
            else:
                v = variant_hit(h)
                out.append(("R5" if v else "R3", j + 1,
                            f"### {h!r} under '{OPP}' is not a vocabulary value"
                            + (f" (variant of /{v}/)" if v else "")))
        dupe = [r for r in set(seen) if seen.count(r) > 1]
        if dupe:
            out.append(("R3", start + 1, f"region repeated under one heading: {dupe}"))
        # R6: a region with no subsection is SILENT, and the ingest brief is explicit
        # that silence looks exactly like coverage. An informed gap must be written
        # down; an absent heading writes nothing down.
        # D6 (p774): R6 is guarded on `seen` being non-empty on purpose. A block whose
        # headings are ALL unrecognised has already been fully reported by R3/R5, and
        # firing R6 as well would report one defect twice and inflate the count -- the
        # exact inflation p772's D6/D7/D10 produced.
        missing = [v for v in VOCAB if v not in seen]
        if seen and missing:
            out.append(("R6", start + 1,
                        f"live block covers {len(seen)}/5 of the closed vocabulary; "
                        f"SILENT: {missing}. The brief requires an explicit gap, not an "
                        "absent subsection"))
    return out

# ------------------------- controls -------------------------------------
def controls():
    ok = lambda t: scan("K", t)
    good_fm = "---\nindustry: education\nregion: Global\nupdated: 2026-11-11\n---\n"
    five = "".join(f"### {r}\n\nprose\n\n" for r in VOCAB)
    T = []
    T.append(("K1 clean file, 5 correct region blocks",
              good_fm + f"\n{OPP}\n\n" + five, []))
    # D1 (p774, this gate's own): a CASE variant and a LEXICAL variant are not the
    # same defect. "Latam" lowercases INTO the vocabulary, so it is a second-bucket
    # case drift (R2/R3); "Europe" does not, so it is R5. The first write of these
    # two controls asserted R5 for both and the gate was right and the control wrong.
    T.append(("K2 frontmatter 'Latam' is a CASE variant -> second bucket",
              good_fm.replace("region: Global", "region: Latam"), ["R2"]))
    T.append(("K3 no frontmatter at all",
              f"# title\n\n{OPP}\n\n" + five, ["R1"]))
    T.append(("K4 '### LatAm' under Opportunities is a CASE variant",
              good_fm + f"\n{OPP}\n\n### LatAm\n\nprose\n", ["R3", "R6"]))
    T.append(("K5 C-fence: a ## heading inside a code fence is not a heading",
              good_fm + f"\n```\n{OPP}\n### Latam\n```\n", []))
    T.append(("K6 two Opportunities headings",
              good_fm + f"\n{OPP}\n\n" + five + f"\n{OPP}\n\n" + five, ["R4"]))
    T.append(("K7 C-scope: '### North America' under a DIFFERENT ## is prose",
              good_fm + "\n## Market map\n\n### North America\n\nprose\n", []))
    T.append(("K8 C-menu: the brief's template line shipped as data",
              good_fm.replace("region: Global",
                              "region: North America | EMEA | APAC | LATAM | Global"),
              ["R2"]))
    T.append(("K9 C-quote: region: \"LATAM\" is the same value",
              good_fm.replace("region: Global", 'region: "LATAM"'), []))
    T.append(("K10 C-depth: #### under Opportunities is not a ### block",
              good_fm + f"\n{OPP}\n\n### LATAM\n\n#### Brazil\n\nprose\n", ["R6"]))
    T.append(("K11 case drift 'latam' is a second bucket",
              good_fm.replace("region: Global", "region: latam"), ["R2"]))
    # D5 (p774, this gate's own): once R4 counts only BARE headings, a file whose
    # ONLY opportunities heading is qualified has declared itself all-history and has
    # no live block -- so there is nothing for R6 to find incomplete. Asserting R6
    # here would demand a live block this base's own convention does not require.
    T.append(("K12 D5: a qualified-only heading declares history, so no live block",
              good_fm + "\n## Opportunities by region (LATAM)\n\n### LATAM\n\np\n", []))
    T.append(("K13 a LEXICAL variant must still be caught: '### Europe'",
              good_fm + f"\n{OPP}\n\n### Europe\n\nprose\n", ["R5"]))
    T.append(("K17 D4: a QUALIFIED heading is this base's supersession convention",
              good_fm + f"\n{OPP}\n\n" + five
              + "\n## Opportunities by region - p769\n\n### North America\n\nprose\n", []))
    T.append(("K18 R6: the live block drops a region and goes silent on it",
              good_fm + f"\n{OPP}\n\n"
              + "".join(f"### {r}\n\nprose\n\n" for r in VOCAB if r != "Global"), ["R6"]))
    T.append(("K15 D2: a narrative pass heading holding both words is not the heading",
              good_fm + "\n## `p602` - the mandated legs: all 5 opportunity "
              "subsections updated, no region silent\n\nprose\n", []))
    T.append(("K16 D3: a ###-level '(historical) Opportunities by region' marker is history",
              good_fm + "\n### (historical) Opportunities by region - superseded, "
              "retained for history\n\nprose\n", []))
    T.append(("K14 repeated region under one heading",
              good_fm + f"\n{OPP}\n\n### LATAM\n\np\n\n### LATAM\n\np\n", ["R3", "R6"]))
    fails = []
    for nm, txt, want in T:
        got = sorted({c for c, _, _ in ok(txt)})
        if got != sorted(set(want)):
            fails.append(f"{nm}: want {sorted(set(want))} got {got}")
    return fails, len(T)

if __name__ == "__main__":
    args = sys.argv[1:]
    if not args or args[0] == "--controls":
        f, n = controls()
        print(f"gate-regions CONTROLS: {n-len(f)}/{n} pass")
        for x in f:
            print("  FAIL", x)
        sys.exit(2 if f else 0)
    f, n = controls()
    if f:
        print(f"REFUSING TO RUN: {len(f)}/{n} controls fail")
        for x in f:
            print("  FAIL", x)
        sys.exit(2)
    print(f"gate-regions CONTROLS: {n}/{n} pass\n")
    tot = 0
    perfile = {}
    for p in args:
        try:
            t = open(p, encoding="utf-8", errors="replace").read()
        except Exception as e:
            print(f"READ-FAIL\t{p}\t{e}")
            continue
        d = scan(p, t)
        if d:
            perfile[p] = d
            tot += len(d)
    for p in sorted(perfile):
        for c, ln, detail in perfile[p]:
            print(f"{c}\t{p}:{ln}\t{detail}")
    print(f"\nFILES SCANNED {len(args)} · FILES WITH DEFECTS {len(perfile)} · DEFECTS {tot}")
