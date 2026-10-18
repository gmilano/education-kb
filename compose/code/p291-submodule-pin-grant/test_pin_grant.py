"""Controls for `ACTION p291`. Run from this directory: `python3 test_pin_grant.py`."""
import sys
from pin_grant import (classify, parse_tsv, census, VERDICTS,
                       shelf_claims_text, blocks, latest_pass_section)

PIN = "1a2d898bbd04ffd60498bb23a4aa14e3eb5f8a66"
OTHER = "54ee9d91eecd964fc100f4ec4bb2dbf500c82985"
PAY = "f1269b7b2313"

FAILED = []


def check(name, got, want):
    ok = got == want
    if not ok:
        FAILED.append(f"{name}: got {got!r} want {want!r}")
    print(f"  {'🟢' if ok else '🔴'} {name}")


def row(**kw):
    base = dict(superproject="iblai/iblai-claw-agents", submodule_path="higher-education",
                submodule_slug="iblai/higher-education-agents", pinned_gitlink_sha=PIN,
                read_at_ref=PIN, payload_path="LICENSE", payload_bytes="1063",
                payload_sha256_12=PAY, family="MIT", verdict="GRANTED-AT-PIN")
    base.update(kw)
    return base


def nfind(r):
    return len(classify(r)[1])


print("── p291-submodule-pin-grant")

# --- the happy path -----------------------------------------------------------------
check("C1 read AT the pin with a payload digest is clean", nfind(row()), 0)

# --- ACTION p291's own correction of p290 -------------------------------------------
check("C7 GRANTED-AT-PIN read at HEAD is REJECTED even though p290 allowed it",
      nfind(row(read_at_ref="HEAD")), 1)
check("C7b read at 'main' is the same defect", nfind(row(read_at_ref="main")), 1)
check("C7c an unrecorded read ref is the same defect", nfind(row(read_at_ref="")), 1)
check("C8 read at a REAL commit that is not the pin is rejected",
      nfind(row(read_at_ref=OTHER)), 1)

# --- the verdict vocabulary stays closed --------------------------------------------
check("C2 a verdict outside the vocabulary fails", nfind(row(verdict="GRANTED")), 1)
check("C2b every listed verdict is accepted on a well-formed row",
      sum(nfind(row(verdict=v,
                    payload_sha256_12=PAY if v == "GRANTED-AT-PIN" else "-"))
          for v in VERDICTS), 0)

# --- a grant verdict must rest on a payload -----------------------------------------
check("C3 GRANTED-AT-PIN with no payload digest fails",
      nfind(row(payload_sha256_12="")), 1)
check("C3b GRANTED-AT-PIN with a non-digest placeholder fails",
      nfind(row(payload_sha256_12="-")), 1)
check("C4 NO-GRANT-AT-PIN carrying a payload digest fails",
      nfind(row(verdict="NO-GRANT-AT-PIN")), 1)
check("C4b NO-GRANT-AT-PIN with no digest is clean",
      nfind(row(verdict="NO-GRANT-AT-PIN", payload_sha256_12="-")), 0)

# --- a pin must be an exact commit ---------------------------------------------------
check("C5 a short pin is not a pin", nfind(row(pinned_gitlink_sha="1a2d898bbd04",
                                               read_at_ref="1a2d898bbd04")), 1)
check("C5b a branch name is not a pin", nfind(row(pinned_gitlink_sha="main",
                                                  read_at_ref="main")), 2)

# --- UNPROBED is honest, never a pass ------------------------------------------------
check("C6 UNPROBED needs no payload and no read ref",
      nfind(row(verdict="UNPROBED", read_at_ref="", payload_sha256_12="-")), 0)

# --- the census: p290's actual residue ------------------------------------------------
SEVEN = "higher-education,k-12,enterprise,government,legal,financial-services,medical-healthcare"
two = [row(submodule_path=p, declares_submodule_paths=SEVEN)
       for p in ("higher-education", "k-12")]
check("C9 2 rows against 7 declared submodules is a finding (p290's shape)",
      len(census(two)), 1)
seven = [row(submodule_path=p, declares_submodule_paths=SEVEN) for p in SEVEN.split(",")]
check("C9b 7 rows against 7 declared submodules is clean", len(census(seven)), 0)
check("C9c an UNPROBED row still DISCHARGES the census -- declaring is the duty",
      len(census([row(submodule_path=p, declares_submodule_paths=SEVEN,
                      verdict="UNPROBED" if p != "k-12" else "GRANTED-AT-PIN")
                  for p in SEVEN.split(",")])), 0)

# --- the parser ------------------------------------------------------------------------
TSV = (
    "# a comment\n"
    "superproject\tsubmodule_path\tverdict\n"
    "a/b\thigher-education\tGRANTED-AT-PIN\n"
    "\n"
    "# another comment mid-file\n"
    "a/b\tk-12\tUNPROBED\n"
)
p = parse_tsv(TSV)
check("C10 comments and blank lines are not rows", len(p), 2)
check("C10b the header binds by name", p[1]["verdict"], "UNPROBED")

# --- the shelf arm: BLOCK scope, not line scope -------------------------------------
BEARING = ["iblai/iblai-claw-agents", "iblai/claws"]


def sc(text, shelf="agents/top.md"):
    return len(shelf_claims_text(text, BEARING, shelf))


check("C11 a bare citation with no boundary anywhere is a finding",
      sc("Nine of nine MIT: `iblai/claws` (15 stars), `iblai/os` (821 stars)."), 1)
check("C12 the boundary named on a LATER line of the SAME block clears it",
      sc("The grant is not the one on `iblai/iblai-claw-agents`.\n"
         "That repository is a 13-file shell whose directories are `160000 commit` gitlinks."), 0)
check("C13 the boundary in a DIFFERENT block does NOT clear it",
      sc("Nine of nine MIT: `iblai/claws`.\n\nSeparately: submodules are gitlinks."), 1)
check("C14 p291's own first-draft false positive, verbatim, now clears",
      sc("🔵 The MIT grant that matters is **not** the one on\n"
         "[`iblai/iblai-claw-agents`](https://github.com/iblai/iblai-claw-agents). "
         "That repository is a\n13-file shell whose segment directories are "
         "**`160000 commit` gitlinks**."), 0)
check("C15 plain-words boundary ('pointer ... separate repositories') clears",
      sc("🔴 `iblai/claws` is not what pass 243 published it as. It is a pointer; the seven "
         "sector configurations are **separate repositories**."), 1 - 1)
check("C16 two bearing slugs in one unguarded block are two findings",
      sc("`iblai/claws` and `iblai/iblai-claw-agents` are both MIT."), 2)

# --- the append-only scope ------------------------------------------------------------
TREND = ("## Pass 291 — today\n\nLive text citing `iblai/claws` with no boundary.\n"
         "\n## Pass 243 — history\n\nOld text citing `iblai/claws` with no boundary.\n")
sec, off = latest_pass_section(TREND)
check("C17 the live section stops at the next `## Pass`", "Pass 243" in sec, False)
check("C18 history below the live section is NOT scanned",
      len(shelf_claims_text(sec, BEARING, "agents/trending.md", off)), 1)
check("C19 the offset keeps reported line numbers file-absolute",
      shelf_claims_text(sec, BEARING, "agents/trending.md", off)[0].startswith(
          "agents/trending.md:3:"), True)
check("C20 a file with no `## Pass` heading degrades to whole-file scope",
      latest_pass_section("plain text")[1], 0)

# --- the block splitter ------------------------------------------------------------------
b = blocks("a\nb\n\n\nc\n")
check("C21 consecutive blank lines do not emit empty blocks", len(b), 2)
check("C22 block line numbers are 1-based and point at the first line",
      [n for n, _ in b], [1, 5])

print()
if FAILED:
    print(f"🔴 {len(FAILED)} control(s) FAILED:")
    for f in FAILED:
        print(f"   {f}")
    sys.exit(1)
print("   PASS")
