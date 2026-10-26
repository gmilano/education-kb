#!/usr/bin/env python3
"""p456 controls -- run in BOTH directions, as every pass since `p446` requires.

`make hooks` is denied on this host (`Code from External`), so nothing this
pass publishes is gate-attested. These controls are the substitute: each one
asserts a fact that would FAIL if the instrument were broken, and several
assert payload digests EARLIER PASSES published, so a regression in the read
channel is caught against the shelves' own history rather than against itself.

Run:  python3 controls.py
"""
import re
import sys

import resolve
from family_version import family, only_or_later, compatible
from fetch import raw, digest

PASS = FAIL = 0


def check(name, got, want):
    global PASS, FAIL
    ok = got == want
    PASS, FAIL = PASS + ok, FAIL + (not ok)
    print(f"  {'ok  ' if ok else 'FAIL'} {name}")
    if not ok:
        print(f"       got {got!r} want {want!r}")


def truthy(name, got):
    global PASS, FAIL
    PASS, FAIL = PASS + bool(got), FAIL + (not got)
    print(f"  {'ok  ' if got else 'FAIL'} {name}")


MIT = ("MIT License\n\nCopyright (c) 2026 X\n\nPermission is hereby granted, "
       "free of charge, to any person obtaining a copy\nof this software")
GPL2 = ("GNU GENERAL PUBLIC LICENSE\n Version 2, June 1991\n\nThis program is "
        "free software; you can redistribute it")
GPL3 = ("GNU GENERAL PUBLIC LICENSE\n Version 3, 29 June 2007\n\nEveryone is "
        "permitted to copy")

print("\n-- A. licence reader, both directions (carried from p455, re-asserted) --")
check("MIT payload grades MIT", family(MIT), "MIT")
check("GPLv2 payload grades GPL-2.0", family(GPL2), "GPL-2.0")
check("GPLv2 is NOT graded LGPL", family(GPL2).startswith("LGPL"), False)
check("GPLv3 payload grades GPL-3.0", family(GPL3), "GPL-3.0")
check("GPL-2.0 vs GPL-3.0 incompatible", compatible("GPL-2.0", "GPL-3.0"), False)
# `family()` returns the TYPED miss `UNREAD` rather than echoing the payload.
# That is the safe direction and the reason `Gap 453-E` exists: `p455`'s
# `canon()` fell through to `return grade.strip()`, so an ungated reader could
# publish the string `404: Not Found` as a licence grade. These two assert the
# typed miss in both directions -- a reader that echoed the body would fail.
check("404 body grades as a typed miss, not a licence",
      family("404: Not Found"), "UNREAD")
check("404 body is NOT echoed back as its own grade",
      family("404: Not Found") == "404: Not Found", False)
check("empty payload grades as a typed miss", family(""), "UNREAD")

print("\n-- B. ls_remote: the new channel, both directions --")
d, heads, tags = resolve.ls_remote("bain3/pronotepy")
check("pronotepy default branch is master", d, "master")
truthy("pronotepy reports >=1 head", len(heads) >= 1)
d2, h2, t2 = resolve.ls_remote("nope-p456-ref-resolution/nope-p456")
check("fabricated address resolves nothing", (d2, h2), (None, []))
d3, h3, _ = resolve.ls_remote("lanis-mobile/LanisAPI")
check("LanisAPI default is deprecation-notice", d3, "deprecation-notice")
check("LanisAPI has NO master head", "master" in h3, False)

print("\n-- C. `Gap 455-A` refuted: HEAD follows the default branch --")
for addr, want_default in [("lanis-mobile/LanisAPI", "deprecation-notice"),
                           ("ILIAS-eLearning/ILIAS", "release_11"),
                           ("overhangio/tutor", "release")]:
    dd, hh, tt, head_sha, head_shas = resolve.ls_remote(addr, want_sha=True)
    check(f"{addr}: HEAD sha == default sha", head_sha == head_shas.get(dd), True)
    check(f"{addr}: default is {want_default}", dd, want_default)

print("\n-- D. digests EARLIER passes published (regression guard on the channel) --")
for addr, ref, path, nbytes, sha, who in [
    ("bain3/pronotepy", "master", "LICENSE", 1062, "4f074ab7dccb", "p455"),
    ("lanis-mobile/LanisAPI", "deprecated-0.4.1", "LICENSE", 1076,
     "0bc449776673", "p455 (as `master`)"),
    ("SchoolUtils/WebUntis", "HEAD", "License", 1070, "d2e54565d9bf", "p455"),
]:
    st, body = raw(addr, ref, path)
    check(f"{who}: {addr}@{ref}/{path} = {nbytes} B {sha}",
          (st, len(body), digest(body)), (200, nbytes, sha))

print("\n-- E. the verdict classes this pass adds --")
check("LanisAPI is GRANT_OFF_DEFAULT",
      resolve.grant("lanis-mobile/LanisAPI")["verdict"], "GRANT_OFF_DEFAULT")
check("its successor is GRANT_AT_DEFAULT",
      resolve.grant("lanis-mobile/liblanis-for-python")["verdict"],
      "GRANT_AT_DEFAULT")
check("tosuki/moodle-mcp serves NO grant at default",
      resolve.grant("tosuki/moodle-mcp")["verdict"], "LIVE_NO_GRANT")
check("fabricated address is ADDRESS_DEAD",
      resolve.grant("nope-p456-ref-resolution/nope-p456")["verdict"],
      "ADDRESS_DEAD")

print("\n-- F. `p455`'s digest-lineage rule, narrowed by measurement --")
# p455: "both serve the stock GPL-3.0 text, so a digest match here is evidence
# of a stock payload and NEVER of shared lineage". True for GPL. FALSE for MIT:
# MIT's payload embeds the holder, so an identical digest names the SAME holder.
st_f, b_f = raw("falkenslab/moodle-mcp", "HEAD", "LICENSE")
st_t, b_t = raw("triffon/moodle-mcp", "HEAD", "LICENSE")
check("falkenslab and triffon MIT digests are identical",
      digest(b_f) == digest(b_t), True)


def holder(b):
    m = re.search(rb"(?im)^copyright \(c\) .*$", b)
    return m.group(0).decode() if m else ""


check("...and the holder is the SAME string (so it IS lineage)",
      holder(b_f) == holder(b_t), True)
check("the fork ships UPSTREAM's holder, not its own",
      "Falkenslab" in holder(b_t), True)
st_g, b_g = raw("lanis-mobile/lanis-rs", "HEAD", "LICENSE")
check("stock GPL-3.0 payload carries NO holder line",
      bool(re.search(rb"(?im)^copyright \(c\) [0-9]", b_g)), False)

print("\n-- G. forward grant is never guessed --")
check("MIT has no GNU forward grant", only_or_later(MIT), "UNSTATED")

print(f"\n{PASS} passed, {FAIL} failed")
sys.exit(1 if FAIL else 0)
