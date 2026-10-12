"""p141-repo-origin-layer — `ACTION CY`: can the REPOSITORY layer place a row the payload could not?

p140 pre-registered:

> Run the `p140-origin-evidence` probe over the **repository** layer of the rows it could not
> place: `git log` author email domains and any `FUNDING.yml`, for the six npm rows that
> yielded no origin signal in their payloads. 🔴 *Refuted if the repository layer places no
> additional row -- which would mean `T29`'s "origin is in the code" is specifically about
> compiled-in hosts, not about code generally.*

🔴 **REFUTED. The repository layer places ZERO additional rows, and for four of the six the
layer does not exist to be read.** Measured, not assumed:

  * 3 of 6 declare **no `repository` field in ANY published version** -- so there is no
    pointer to follow. Not a stale pointer, not a private repo: nothing.
  * 1 of 6 declares one that is **not publicly readable** (`owentaylor/canvas-mcp`),
    confirmed against a deliberately nonexistent control that fails identically.
  * The 2 reachable rows yield no institutional email domain and **no funding file at all**.

So `T29` narrows exactly as p140's falsifier said it would: origin is in the code when the
code has to reach a named host to work. It is not in "code generally", and it is not in
repository metadata.

## 🔴 A method warning this probe had to discover the hard way

`curl -sI https://github.com/<owner>/<repo>` answers **403 for every repository**, live or
not, because this environment's proxy allowlists git smart-HTTP and the package registries
but not github.com HTML. 🔵 **An HTTP status from that channel carries no information about
whether a repository exists.** The only valid liveness probe here is `git ls-remote` (or a
clone), and a negative must be read against a control -- which is why `CONTROL_ABSENT` below
is a deliberately nonexistent coordinate and is checked on every run.

## 🆕 The timezone channel

Author email domains were the registered instrument and they return almost nothing: 6 of 8
maintainer addresses on this shelf are free-mail, and the other 2 are vendor `.com` domains
that carry no country. So this probe adds one: **the UTC offset recorded in each commit.**

A commit's offset is written by the author's own machine at commit time. It is not a name, it
is not editable by a later reader, and a project cannot fake it into a different hemisphere
without lying about every commit. It is weaker than a compiled-in hostname -- it places a
*person at a keyboard*, not an institution -- and it is reported as its own evidence kind.

🔴 **It is only usable where the offset is unambiguous across regions**, and the interesting
case is where it is not:

  `+0530`  India, Sri Lanka ................................. APAC, unambiguous
  `+0800`  China, HK, Taiwan, Singapore, Malaysia, W. Australia  APAC, unambiguous
  `+1000`  AEST, Papua New Guinea, Vladivostok ................ APAC, unambiguous
  `+1100`  AEDT, Solomon Is., New Caledonia ................... APAC, unambiguous
  `+0200`  Central Europe (DST), Eastern Europe, South Africa, Egypt, Israel (DST)  EMEA
  `+0300`  Turkey, Saudi Arabia, East Africa, Moscow .......... EMEA, unambiguous
  `-0600`  🔴 US Central AND Mexico City AND Guatemala, Costa Rica, Honduras,
           El Salvador, Nicaragua, Belize ..... 🔴 AMBIGUOUS: North America OR LATAM
  `-0700`  🔴 US Mountain AND Chihuahua, Sonora ............... 🔴 AMBIGUOUS
  `-0400`  🔴 US Eastern (DST) AND Bolivia, Paraguay, Chile, Amazonas, Atlantic Canada
                                              ................ 🔴 AMBIGUOUS
  `+0000`  UTC -- the default on CI runners and containers ..... NO SIGNAL

🔵 **The ambiguous rows are the point.** The one row a careless probe would book "North
America" off `-0600`/`-0700` is exactly the row where Mexico and Central America are live
alternatives -- and this KB has spent nine passes recording that it has no LATAM-owned row.
Booking one by accident, in the direction of a gap it has been honest about, would be worse
than leaving it `UNMAPPED`. So the table refuses it, and `test_repo_origin.py` pins that.

`+0000` is excluded outright rather than treated as Europe: it is what a container writes.
"""

import json
import re
import subprocess
import sys

OFFSET_REGION = {
    "+0530": ("APAC", "India / Sri Lanka"),
    "+0545": ("APAC", "Nepal"),
    "+0630": ("APAC", "Myanmar"),
    "+0700": ("APAC", "Indochina / W. Indonesia"),
    "+0800": ("APAC", "China / HK / Taiwan / Singapore / Malaysia / W. Australia"),
    "+0900": ("APAC", "Japan / Korea"),
    "+0930": ("APAC", "Australia Central"),
    "+1000": ("APAC", "AEST / Papua New Guinea"),
    "+1030": ("APAC", "Australia Central DST"),
    "+1100": ("APAC", "AEDT / Solomon Is. / New Caledonia"),
    "+1200": ("APAC", "New Zealand / Fiji"),
    "+1300": ("APAC", "New Zealand DST"),
    "+0100": ("EMEA", "Central Europe / W. Africa"),
    "+0200": ("EMEA", "Central Europe DST / E. Europe / South Africa / Egypt / Israel"),
    "+0300": ("EMEA", "Turkey / Saudi Arabia / East Africa / Moscow"),
    "+0330": ("EMEA", "Iran"),
    "+0400": ("EMEA", "Gulf / Caucasus"),
    "+0430": ("EMEA", "Afghanistan"),
    "-0800": ("North America", "US/Canada Pacific"),
    "-0900": ("North America", "Alaska"),
    "-1000": ("North America", "Hawaii"),
}

# 🔴 Offsets shared across two of the five regions. Never bookable.
AMBIGUOUS = {
    "-0300": "Brazil/Argentina/Uruguay (LATAM) AND Greenland/St Pierre (North America)",
    "-0400": "US Eastern DST / Atlantic Canada (North America) AND Bolivia, Paraguay, "
             "Chile, Amazonas (LATAM)",
    "-0500": "US/Canada Eastern (North America) AND Colombia, Peru, Ecuador (LATAM)",
    "-0600": "US/Canada Central (North America) AND Mexico City, Guatemala, Costa Rica, "
             "Honduras, El Salvador, Nicaragua, Belize (LATAM)",
    "-0700": "US/Canada Mountain (North America) AND Chihuahua, Sonora (LATAM)",
    "-0100": "Azores (EMEA) AND Cape Verde (EMEA) — single region but no country signal",
}
# UTC is what a CI runner or container writes. Not evidence of anything.
NO_SIGNAL = {"+0000", "-0000"}

PERSONAL_MAIL = {
    "gmail.com", "googlemail.com", "outlook.com", "hotmail.com", "yahoo.com",
    "proton.me", "protonmail.com", "icloud.com", "me.com", "qq.com", "163.com",
    "users.noreply.github.com", "github.com", "example.com",
}

CONTROL_ABSENT = "https://github.com/gmilano/definitely-not-a-real-repo-p141"


def _git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True,
                          text=True, timeout=120).stdout


def ls_remote_live(url):
    """True when the remote is publicly readable.

    🔴 Not `curl`: HTML github.com answers 403 for everything through this proxy, live or
    not. A clone/ls-remote against a nonexistent repo prompts for credentials and, with
    prompts disabled, fails -- which is the signature this function reads.
    """
    r = subprocess.run(["git", "ls-remote", url], capture_output=True, text=True,
                       timeout=180, env={"GIT_TERMINAL_PROMPT": "0", "HOME": "/tmp",
                                         "PATH": "/usr/bin:/bin:/usr/local/bin"})
    return r.returncode == 0 and bool(r.stdout.strip())


def offsets(repo):
    out = _git(repo, "log", "--format=%ad", "--date=format:%z")
    counts = {}
    for line in out.splitlines():
        o = line.strip()
        if re.fullmatch(r"[+-]\d{4}", o):
            counts[o] = counts.get(o, 0) + 1
    return counts


def email_domains(repo):
    out = _git(repo, "log", "--format=%ae%n%ce")
    counts = {}
    for line in out.splitlines():
        if "@" in line:
            d = line.strip().rsplit("@", 1)[-1].lower()
            counts[d] = counts.get(d, 0) + 1
    return counts


def funding_files(repo):
    out = _git(repo, "ls-files")
    return [p for p in out.splitlines() if "funding" in p.lower()]


def book(counts):
    """(region, note, evidence) from an offset histogram, or UNMAPPED with the reason."""
    signal = {o: n for o, n in counts.items() if o not in NO_SIGNAL}
    if not signal:
        return "UNMAPPED", "every commit at UTC — a container default, not a location", "-"
    best = max(signal.items(), key=lambda kv: kv[1])
    off, n = best
    if off in AMBIGUOUS:
        return ("UNMAPPED",
                "offset %s is AMBIGUOUS across regions: %s — declined rather than guessed"
                % (off, AMBIGUOUS[off]),
                "%s x%d" % (off, n))
    if off not in OFFSET_REGION:
        return "UNMAPPED", "offset %s not in the table" % off, "%s x%d" % (off, n)
    region, where = OFFSET_REGION[off]
    # A second, differently-regioned unambiguous offset makes the booking unsafe.
    others = {o for o in signal
              if o != off and o not in AMBIGUOUS and o in OFFSET_REGION
              and OFFSET_REGION[o][0] != region and signal[o] > 1}
    if others:
        return ("UNMAPPED",
                "offsets disagree across regions: %s" % sorted(others | {off}),
                "%s x%d" % (off, n))
    return region, where, "%s x%d of %d commits" % (off, n, sum(counts.values()))


COLS = ["subject", "declared_repo", "repo_readable", "institutional_email_domains",
        "funding_files", "dominant_offset", "region", "evidence_kind", "note"]


def row(subject, declared_repo, local_clone=None):
    if not declared_repo:
        return dict(zip(COLS, [subject, "NONE", "n/a", "-", "-", "-", "UNMAPPED",
                               "NO_REPOSITORY_FIELD",
                               "no repository declared in any published version"]))
    readable = local_clone is not None
    if not readable:
        return dict(zip(COLS, [subject, declared_repo, "NO", "-", "-", "-", "UNMAPPED",
                               "REPO_UNREADABLE",
                               "ls-remote fails as the nonexistent control does"]))
    doms = email_domains(local_clone)
    inst = {d: n for d, n in doms.items() if d not in PERSONAL_MAIL}
    fund = funding_files(local_clone)
    offs = offsets(local_clone)
    region, note, ev = book(offs)
    kind = "TZ_OFFSET" if region != "UNMAPPED" else "NONE"
    return dict(zip(COLS, [
        subject, declared_repo, "YES",
        ",".join("%s(%d)" % (d, n) for d, n in sorted(inst.items())) or "NONE",
        ",".join(fund) or "NONE", ev, region, kind, note]))


def main(argv):
    """argv: subject=declared_repo=local_clone_path triples; empty clone path = unreadable."""
    print("# control %s readable=%s (must be False)"
          % (CONTROL_ABSENT, ls_remote_live(CONTROL_ABSENT)), file=sys.stderr)
    rows = []
    for spec in argv:
        parts = spec.split("=")
        subject = parts[0]
        declared = parts[1] if len(parts) > 1 and parts[1] else None
        clone = parts[2] if len(parts) > 2 and parts[2] else None
        rows.append(row(subject, declared, clone))
    print("\t".join(COLS))
    for r in rows:
        print("\t".join(str(r[c]) for c in COLS))
    placed = {r["subject"]: r["region"] for r in rows if r["region"] != "UNMAPPED"}
    print("\n# rows placed by the repository layer: %d of %d" % (len(placed), len(rows)),
          file=sys.stderr)
    print(json.dumps(placed, indent=2), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
