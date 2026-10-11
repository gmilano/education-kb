#!/usr/bin/env python3
"""p135 instrument — licence identity by sha256 over normalised payloads.

Replaces substring licence detection (the lane p134's `ACTION BP` retired) with
hash matching against canonical SPDX texts.

Why a raw sha256 of a LICENSE file is useless on its own: every real MIT file
carries a copyright line the SPDX template leaves as a placeholder, so a real
MIT payload NEVER hashes to the canonical MIT text. The instrument therefore
hashes three progressively normalised forms and reports WHICH form matched:

  raw      sha256 of the bytes as served
  ws       + CRLF->LF, trailing whitespace per line stripped, trailing blank
             lines dropped, FSF's http://->https:// update applied
  flow     + each paragraph reflowed to one line (hard line breaks collapsed)
  body     + copyright/placeholder lines removed

The `flow` level is the one that actually does the work, and finding that out
was this pass's result. SPDX wraps its canonical texts at ~105 columns; real
LICENSE files wrap at ~72. Same words, different hard line breaks, so neither
the raw bytes nor a whitespace-normalised form ever matches. Licence payloads
are not whitespace variants of the canonical text -- they are REFLOWED copies.

Verdicts, strongest first:
  EXACT              raw bytes identical to the canonical text
  WHITESPACE_VARIANT identical once whitespace/URL-normalised
  REFLOWED           identical once paragraphs are reflowed (wrap width only)
  TEMPLATE_MATCH     identical once reflowed AND the copyright line removed --
                     the normal case for a correctly applied MIT/BSD licence
  MODIFIED_SUPERSET  contains the whole canonical body AND extra clauses --
                     the P134-F class ("MIT + a visible-attribution clause")
  UNMATCHED          no canonical text accounts for it

It also groups payloads by `body` hash across owners, which is how a mirrored
repo is told from an independent implementation.
"""

import hashlib
import re
import sys
from pathlib import Path

# A copyright notice is removed as a SPAN inside an already-reflowed paragraph,
# never as a whole line. Line-based stripping is wrap-dependent in both possible
# orders and corrupts the text either way:
#   strip after reflow  -> the GNU header's "Everyone is permitted to copy..."
#                          shares the notice's paragraph and is deleted with it
#   strip before reflow -> a 72-column Apache payload breaks mid-sentence before
#                          the word "copyright", so the continuation line
#                          "copyright notice that is included in..." is deleted
# Both were observed on real payloads in this corpus, and both silently removed
# licence text rather than failing loudly.
#
# The span runs from "Copyright" to the end of its paragraph, or stops earlier
# at an angle-bracketed address followed by a new sentence -- which is what ends
# the FSF notice ("... Inc. <https://fsf.org/> Everyone is permitted ...")
# without stopping inside MIT's own "<year> <copyright holders>" placeholders.
# Anchored at the paragraph start AND required to carry a year or an SPDX
# placeholder. Without both guards the bare word "copyright" mid-sentence
# matches -- Apache-2.0 contains "a readable copyright notice that is included
# in or attached to the work", and deleting from there removed a clause.
COPYRIGHT_SPAN_RE = re.compile(
    rb"^Copyright\s*(?:\((?:c|C)\)|\xc2\xa9)?\s*"
    rb"(?:\[?\d{4}\]?(?:\s*[-,]\s*\d{4})*|<year>|\[yyyy\])"
    rb"[^\n]*?(?:(?<=[>/}\)])(?=\s+[A-Z][a-z])|$)",
    re.IGNORECASE,
)

# Typographic variants that carry no legal meaning. SPDX's canonical GPL-3.0
# uses curly quotes; the COPYING file shipped in real repositories uses ASCII
# ones, and that single character class was the whole difference on five
# payloads in this corpus. Dashes are folded for the same reason.
PUNCT_MAP = [
    ("“", '"'), ("”", '"'), ("‘", "'"), ("’", "'"),
    ("–", "-"), ("—", "-"), (" ", " "),
    # GNU's "How to Apply" appendix brackets its placeholders. Real COPYING
    # files vary between <one line to give the program's name> and
    # {one line to give the program's name}; adaptlearning/adapt_framework uses
    # braces and is otherwise GPL-3.0 to the character. Folding the bracket
    # style changes no words.
    ("{", "<"), ("}", ">"),
]

# A copyright notice occupying a WHOLE paragraph on its own is stripped even
# without a year: dhodges47/SCORM-LearningManagementSystem carries
# "Copyright (c) David Hodges dba Outermost Software, LLC" with no year at all.
# The year requirement stays for notices embedded in a larger paragraph, where
# it is the only thing separating a notice from prose about copyright.
BARE_NOTICE_RE = re.compile(
    rb"^Copyright\s*(?:\((?:c|C)\)|\xc2\xa9)\s*[^\n]{0,160}$", re.IGNORECASE
)
# The FSF changed its own licence URLs from http:// to https://; GNU payloads
# committed before that update differ from today's canonical text by that alone.
FSF_HTTP_RE = re.compile(rb"http://(www\.)?(gnu|fsf)\.org")

# A SECOND steward-side edit, found by this pass: the FSF moved
# why-not-lgpl.html from /licenses/ to /philosophy/. A GPL-3.0 COPYING file
# committed before that move is otherwise byte-identical to today's canonical
# text, and this one URL path was the whole remaining difference on five
# payloads here -- after punctuation and wrapping had already been normalised.
#
# Declared limitation: normalising steward edits needs a table that grows every
# time a licence steward edits its own text. Two such edits are known for GNU.
# A payload predating a third will read UNMATCHED with a ~0.999 nearest score,
# so a high nearest ratio on a GNU text should be read as "probably a steward
# edit this table has not learnt yet", not as a modified licence.
FSF_MOVED_PATHS = [
    (rb"gnu\.org/licenses/why-not-lgpl", b"gnu.org/philosophy/why-not-lgpl"),
]


def _read(path):
    return Path(path).read_bytes()


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def normalise_ws(data: bytes) -> bytes:
    """CRLF->LF, strip per-line trailing whitespace, drop trailing blank lines,
    normalise FSF http->https. Interior blank lines are preserved."""
    data = FSF_HTTP_RE.sub(lambda m: b"https://" + (m.group(1) or b"") + m.group(2) + b".org", data)
    for pat, dst in FSF_MOVED_PATHS:
        data = re.sub(pat, dst, data)
    for src, dst in PUNCT_MAP:
        data = data.replace(src.encode("utf-8"), dst.encode("ascii"))
    data = data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    lines = [ln.rstrip() for ln in data.split(b"\n")]
    while lines and not lines[-1]:
        lines.pop()
    return b"\n".join(lines)


def reflow(data: bytes) -> bytes:
    """Collapse hard line breaks inside each paragraph so that wrap width stops
    mattering. Paragraph boundaries (blank lines) are preserved, so document
    structure still distinguishes two different licences."""
    paragraphs = re.split(rb"\n[ \t]*\n", data)
    out = []
    for para in paragraphs:
        joined = b" ".join(para.split())
        if joined:
            out.append(joined)
    # Joined with a blank line, not a single newline, so that reflow() is
    # idempotent: its own output must re-parse into the same paragraphs. With a
    # single newline a second pass would merge every paragraph into one, and two
    # licences differing only in structure could then hash alike.
    return b"\n\n".join(out)


def strip_copyright(data: bytes) -> bytes:
    """Remove copyright notices from ALREADY-REFLOWED text, as spans.

    Input must be the output of reflow(), so that every paragraph is one line
    and the span regex cannot be affected by wrap width. Paragraphs left empty
    by the removal are dropped; the rest keep their order and boundaries.
    """
    out = []
    for para in data.split(b"\n\n"):
        if BARE_NOTICE_RE.match(para):
            continue
        cleaned = COPYRIGHT_SPAN_RE.sub(b"", para).strip()
        if cleaned:
            out.append(cleaned)
    return b"\n\n".join(out)


def collapse(data: bytes) -> bytes:
    """Collapse ALL whitespace, paragraph breaks included. The weakest level,
    used only after every structured form has failed: it absorbs title-block
    differences (a licence whose name and version sit on one line rather than
    two). Word order must still match exactly, so two different licences cannot
    collide here -- the risk it carries is only that it hides formatting, which
    is why its verdict is reported separately rather than as a clean match."""
    return b" ".join(data.split())


def hashes(data: bytes) -> dict:
    ws = normalise_ws(data)
    flow = reflow(ws)
    body = strip_copyright(flow)
    return {
        "raw": sha(data),
        "ws": sha(ws),
        "flow": sha(flow),
        "body": sha(body),
        "collapsed": sha(collapse(body)),
        "_body": body,
    }


def strip_frontmatter(data: bytes) -> bytes:
    """Drop a leading YAML frontmatter block. Some canonical texts are taken
    from choosealicense.com, which ships them with metadata on top; hashing
    that metadata would make every comparison fail."""
    if data.startswith(b"---"):
        parts = data.split(b"\n---\n", 1)
        if len(parts) == 2:
            return parts[1].lstrip(b"\n")
    return data


def load_canonical(canon_dir) -> dict:
    canon = {}
    for p in sorted(Path(canon_dir).glob("*.txt")):
        canon[p.stem] = hashes(strip_frontmatter(_read(p)))
    return canon


def classify(payload: bytes, canon: dict):
    """Return (spdx_id, verdict). Prefers the strongest match available."""
    h = hashes(payload)
    best = (None, "UNMATCHED")
    for spdx, c in canon.items():
        if h["raw"] == c["raw"]:
            return spdx, "EXACT"
        if h["ws"] == c["ws"]:
            return spdx, "WHITESPACE_VARIANT"
        if h["flow"] == c["flow"]:
            return spdx, "REFLOWED"
        if h["body"] == c["body"]:
            return spdx, "TEMPLATE_MATCH"
        if h["collapsed"] == c["collapsed"]:
            return spdx, "WHITESPACE_COLLAPSED"
    # Superset check only after every exact form has been ruled out, longest
    # canonical body first so Apache-2.0 wins over a short permissive text.
    for spdx, c in sorted(canon.items(), key=lambda kv: -len(kv[1]["_body"])):
        cb, pb = c["_body"], h["_body"]
        if cb and cb in pb and len(pb) > len(cb):
            return spdx, "MODIFIED_SUPERSET"
    return best


def nearest(h: dict, canon: dict):
    """Closest canonical text by sequence similarity over the normalised body.
    Reported only to explain an UNMATCHED verdict; never used to assert a
    licence, because similarity is not identity -- OpenOLAT's Apache-2.0 with
    two attribution statements appended scores 0.92 and is still not Apache."""
    import difflib

    pb = h["_body"].decode("utf-8", "replace")
    best = ("-", 0.0)
    for spdx, c in canon.items():
        cb = c["_body"].decode("utf-8", "replace")
        ratio = difflib.SequenceMatcher(None, pb, cb).ratio()
        if ratio > best[1]:
            best = (spdx, ratio)
    return best


def main(argv):
    if len(argv) < 3:
        print("usage: licence_sha.py <canonical_dir> <payload_dir> [fetch_log.tsv]", file=sys.stderr)
        return 2
    canon = load_canonical(argv[1])
    if not canon:
        print("no canonical texts found", file=sys.stderr)
        return 2
    rows = []
    by_body = {}
    for p in sorted(Path(argv[2]).glob("*.payload")):
        repo = p.stem.replace("~", "/")
        data = _read(p)
        spdx, verdict = classify(data, canon)
        h = hashes(data)
        near = "-"
        if verdict == "UNMATCHED":
            # An UNMATCHED row with nothing beside it reads as "unusual
            # licence", which is the bias P134-F warned about. Report what it
            # most resembles and how closely, so the reader can tell a modified
            # licence from an unrecognised one.
            spdx_near, ratio = nearest(h, canon)
            near = f"{spdx_near}:{ratio:.3f}"
        rows.append((repo, spdx or "-", verdict, len(data), h["body"][:16], near))
        by_body.setdefault(h["body"], []).append(repo)

    print("repo\tspdx\tverdict\tbytes\tbody_sha16\tnearest")
    for r in rows:
        print("\t".join(str(x) for x in r))

    print("\n# cross-owner identical licence bodies (>1 distinct owner)")
    for body, repos in by_body.items():
        owners = {r.split("/")[0] for r in repos}
        if len(repos) > 1 and len(owners) > 1:
            print(f"{body[:16]}\t{len(repos)} repos\t{len(owners)} owners\t{','.join(sorted(repos))}")

    print("\n# verdict tally")
    tally = {}
    for _, _, v, _, _, _ in rows:
        tally[v] = tally.get(v, 0) + 1
    for v, n in sorted(tally.items(), key=lambda kv: -kv[1]):
        print(f"{v}\t{n}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
