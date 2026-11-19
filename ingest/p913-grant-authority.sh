#!/usr/bin/env bash
# p913 — THE GRANT AUTHORITY.  Retires `p880-licence-byteread.sh` AND supersedes
# `p912-grant-family.sh`.  Discharges `912-G1`.
#
# `912-G1` asked for p880 to be retired against p912's two controls.  Running p912's instrument
# over the whole shelf discharged that and found a THIRD defect, inherited by p912 unchanged, in
# the licence family that matters most to this industry.
#
# ── 913-F1.  EVERY GPL-3.0 PAYLOAD ON THIS SHELF READ AS AGPL-3.0. ──
# GPL-3.0's own text names the Affero licence three times, in section 13 ("Use with the GNU
# Affero General Public License").  Both p880 and p912 grade with:
#     grep -qi "GNU AFFERO GENERAL PUBLIC LICENSE"                        -> AGPL-3.0
#     grep -qi "GNU GENERAL PUBLIC LICENSE" && ! grep -qi "AFFERO|LESSER" -> GPL
# The first line fires on a genuine GPL-3.0 payload and the AFFERO guard then SUPPRESSES the GPL
# branch, so the GPL branch cannot fire on GPL-3.0 at all.  Measured discriminators:
#     true GPL-3.0  : title line `GNU GENERAL PUBLIC LICENSE`,        3 Affero mentions, ~35,147-35,151 B
#     true AGPL-3.0 : title line `GNU AFFERO GENERAL PUBLIC LICENSE`, 15 Affero mentions,  34,523 B
# 🔵 It errs in BOTH directions and both are commercially live.  AGPL-3.0 s.13 imposes a
# NETWORK-USE source-disclosure obligation that GPL-3.0 does not: reporting Koha, Chamilo or ILIAS
# as AGPL OVERSTATES the obligation and wrongly kills a hosted design, while a repository
# published as MIT that is really AGPL (`OpenPronounce/OpenPronounce`) UNDERSTATES it.
#
# ── 913-F2.  THIS IS A REGRESSION OF A FIX THIS BASE ALREADY MADE AND DOCUMENTED. ──
# `ingest/licence-grade-titleline-p640.sh` carries, in its own header comment:
#   "p640 — grade on the TITLE LINE, not substring-over-payload. Both p639's grader and p640's
#    first grader failed on the GNU family because GPL-3.0 names AFFERO 3x (s.13) and AGPL-3.0
#    names 'GNU GENERAL PUBLIC LICENSE' 5x. Title-line grading is the only sound discriminator."
# p880 replaced title-line grading with body-substring grading and reintroduced the defect.  p912
# audited p880 for precisely this collision class (Boost is a PREFIX-COLLISION of the MIT trigger
# phrase) and did not generalise its own rule to the GNU family.  🔴 The process lesson is the
# transferable one: A CORRECTION PASS MUST READ THE INSTRUMENT HISTORY, because the defect it is
# about to find may already have a committed fix that a later instrument dropped.
#
# ── WHAT THIS SCRIPT IS ──  The union of every grant fix this base has made:
#   • p640's TITLE-LINE adjudication, restored, and it is the primary rule (913-F1).
#   • p640's MIT SIZE BAND: an MIT-phrased payload outside ~1000-1250 B is a narrowed derivative.
#   • p912's CREATIVE COMMONS family, which p880 could not see at all (T25, T32).
#   • p912's BOOST-BEFORE-MIT specificity rule (Boost prefix-collides with the MIT phrase).
#   • p880's CUMULATIVE/CONJUNCTIVE detection, kept: a payload may carry more than one grant, and
#     a conjunctive payload is never collapsed to one family.
# The body is consulted ONLY where the title line does not name a licence, and when it is, the
# verdict says so (`BODY-`), because a body verdict is weaker evidence than a title verdict.
set -uo pipefail
OUT="${1:?usage: p913-grant-authority.sh OUT.tsv (then either: slug... | --from-tsv FILE)}"; shift
if [ "$#" -eq 0 ]; then echo "🔴 refusing empty input (Gap 245)" >&2; exit 2; fi

D=$(mktemp -d); trap 'rm -rf "$D"' EXIT
# ── 917-F4.  REVERSED-ORDER FILENAMES.  p913 carried `LICENSE-MIT` but NOT `MIT-LICENSE`, which
# is the Rails/Ruby engine convention (`rails plugin new` emits it).  `PRX/badges_engine` was
# reported NO-LICENCE-FILE-FOUND by p913 and byte-reads as a genuine 1,048 B MIT text at
# `master/MIT-LICENSE` — inside p640's MIT size band.  Measured blast radius: 1 of 13 rows in
# p917's ungranted cohort (7.7%); the other 6 probed carry no reversed-order filename, so the
# defect is real and NARROW.  Added below rather than in a new script, because 913-F2's lesson is
# that a fix living outside the authority is a fix a later instrument drops.
NAMES=(LICENSE LICENSE.txt LICENSE.md LICENSE.TXT LICENCE LICENCE.txt COPYING COPYING.txt
       license license.txt license.md licence licence.txt LICENSE.rst LICENSE-MIT LICENSE-APACHE
       MIT-LICENSE MIT-LICENSE.txt MIT_LICENSE GPL-LICENSE APACHE-LICENSE BSD-LICENSE
       MIT-License.txt COPYRIGHT COPYRIGHT.txt)

# ── 921-F2.  920-G1 DISCHARGED, AND THE REMEDY IT PRESCRIBED IS NOT AVAILABLE IN THIS
# ENVIRONMENT.  `920-G1` asked for "the `LICENSE.*` glob" — but a glob needs a DIRECTORY LISTING,
# and `gh api repos/<owner>/<repo>/contents` returns **403 "GitHub access to this repository is
# not enabled for this session"** for every repository not attached to the session (measured
# p921 on `polm/unidic-lite`).  `raw.githubusercontent.com`, the only open channel, serves an
# EXACT PATH and cannot enumerate.  So the glob is replaced by a NAMED PROBE LIST, and the
# residual blind spot is recorded rather than hidden: a sibling named outside this list is still
# invisible.  Measured fixture: `polm/unidic-lite` carries `LICENSE` (1,051 B, MIT — the
# PACKAGING CODE) and `LICENSE.unidic` (1,515 B, BSD, (c) The UniDic Consortium — THE DICTIONARY
# YOU ACTUALLY INSTALL).  Reading the first and stopping publishes "MIT" over a corpus owned by
# somebody else, which is T25 inside the artefact class this authority exists to cover.
SIBLINGS=(LICENSE.unidic LICENSE.data LICENSE.dataset LICENSE.datasets LICENSE.docs
          LICENSE.doc LICENSE.content LICENSE.model LICENSE.models LICENSE.weights
          LICENSE.media LICENSE.assets LICENSE.fonts LICENSE.images LICENSE.corpus
          LICENSE.dict LICENSE.dictionary LICENSE.third-party LICENSE.third_party
          LICENSE.THIRD-PARTY LICENSE-DATA LICENSE-DOCS LICENSE-CONTENT COPYING.data
          COPYING.LIB COPYING.DOC)

# ---- the adjudicator.  $1 = payload file, $2 = bytes.  Prints "families<TAB>verdict<TAB>note". ----
adjudicate() {
  local B="$1" bytes="$2" title t fam=() v note=""
  title=$(head -c 300 "$B" | tr -d '\357\273\277' | tr '\n' ' ' | sed 's/  */ /g;s/^ //')
  t=$(printf '%s' "$title" | tr '[:upper:]' '[:lower:]')
  # ---- PRIMARY: the title line.  specific-before-generic throughout. ----
  case "$t" in
    *"gnu affero general public license"*)  fam=("AGPL") ;;   # 923-F2: AGPL-1.0 (2002) exists
    *"gnu lesser general public license"*)  fam=("LGPL") ;;
    *"gnu general public license"*)         fam=("GPL") ;;   # 913-F1: reached only via the title
    *"boost software license"*)             fam=("BSL-1.0") ;;
    # ── 923-F1.  SPECIFIC BEFORE GENERIC, AND THE OLDER NAME FIRST.  Apache-1.1 is titled
    # "The Apache Software License, Version 1.1" and Apache-1.0 carries NO licence title at
    # all — only a copyright notice.  Neither contains the string `apache license`, so
    # neither ever reached the version stage `922-F3` fixed.  Measured p923 on the ASF's own
    # published texts: both graded `BSD / BODY-BSD`.  Root only; the version stage decides.
    *"apache software license"*)            fam=("Apache") ;;
    *"apache license"*)                     fam=("Apache") ;;
    *"mozilla public license"*)             fam=("MPL") ;;
    *"educational community license"*)      fam=("ECL") ;;    # 923-F2: ECL-1.0 is OSI-approved
    *"elastic license"*)                    fam=("Elastic") ;;
    # 913-F7: Open Data Commons.  `withmarbleapp/os-taxonomy` is **ODbL** — a share-alike
    # licence for a DATABASE, which is exactly the asset class `T25` says the licence trap moved
    # to.  The shelf published it as `proprietary`.  No prior instrument in this base had a
    # detector for the data-licence family at all.
    *"open database license"*|*"odbl"*)     fam=("ODbL-1.0") ;;
    *"open data commons attribution"*)      fam=("ODC-By") ;;
    *"public domain dedication and license"*|*"odc pddl"*) fam=("PDDL-1.0") ;;
    # 923-F2: EPL and CDDL were named in `922-G2` as families this authority cannot see at
    # all.  Both are versioned and both are weak-copyleft — an EPL row and a CDDL row carry
    # a file-level reciprocity obligation that a `UNKNOWN-TEMPLATE` cell does not state.
    *"eclipse public license"*)             fam=("EPL") ;;
    *"common development and distribution license"*|*"cddl"*) fam=("CDDL") ;;
    *"cc0 1.0 universal"*)                  fam=("CC0-1.0") ;;
    # ── 923-F5.  THE SECOND FAMILY THIS PASS FOUND WITH 923-F1'S DEFECT, AND IT WAS FOUND
    # INDEPENDENTLY, WHICH IS WHY IT IS A RULE AND NOT AN ANECDOTE.  A CC licence's own legal
    # code is titled by its ELEMENTS — `Attribution 4.0 International` — and the words
    # "Creative Commons Attribution" never appear adjacently in the title block.  The only
    # `creative commons` string within the first 300 bytes is the boilerplate disclaimer
    # ("Creative Commons Corporation ... is not a law firm"), so a real CC-BY-4.0 payload fell
    # through to the generic arm.  Measured p923 on `bilalabic/awesome-turkish-datasets`
    # (18,657 B, `sha256_12 9ba9550ad484`): published **`CC-UNSPECIFIED`** where the search
    # channel said CC-BY-4.0 and the bytes agree with the channel.
    # 🔴 THE ORDERING IS LOAD-BEARING, and the old arms had it wrong: `*"attribution-noncommercial"*`
    # preceded any ShareAlike test, so an `Attribution-NonCommercial-ShareAlike` payload was
    # published as `CC-BY-NC` and its SHARE-ALIKE obligation — the one that infects a derived
    # database (`T25`) — was silently dropped.  Specific before generic, longest first.
    *"attribution-noncommercial-sharealike"*)   fam=("CC-BY-NC-SA") ;;
    *"attribution-noncommercial-noderiv"*)      fam=("CC-BY-NC-ND") ;;
    *"attribution-noncommercial"*)              fam=("CC-BY-NC") ;;
    *"attribution-sharealike"*)                 fam=("CC-BY-SA") ;;
    *"attribution-noderiv"*)                    fam=("CC-BY-ND") ;;
    # anchored at the START of the title block: this is the plain CC-BY legal code's own first line.
    attribution\ [0-9]*)                        fam=("CC-BY") ;;
    *"creative commons attribution"*)           fam=("CC-BY") ;;
    *"creative commons"*)                       fam=("CC-UNSPECIFIED") ;;
    # 913-F5: the Mulan family.  `ECNU/EduWork` (East China Normal University) is
    # 木兰宽松许可证 第2版 / Mulan Permissive Software License v2 — OSI-approved, permissive,
    # bilingual, and carrying an Apache-style PATENT grant with litigation-termination that MIT
    # does not have.  p880 and p912 both report it `UNKNOWN-TEMPLATE` (zero detectors), and the
    # shelf published it as **MIT**.  This is the licence family of Chinese education supply,
    # which `T20`/`T29` record as a measured single-country phenomenon, so the blind spot is
    # aimed exactly at the tier this base says is distinctive.
    *"木兰宽松许可证"*|*"mulan permissive software license"*) fam=("MulanPSL") ;;  # 923-F2: v1 exists
    *"木兰公共许可证"*|*"mulan public license"*)              fam=("MulanPubL") ;;  # 923-F2: v1 exists
    *"mit license"*)                        fam=("MIT") ;;
    *"bsd "*|*"bsd-"*)                      fam=("BSD") ;;
    *"isc license"*)                        fam=("ISC") ;;
    *"the unlicense"*|*"unlicense"*)        fam=("Unlicense") ;;
  esac

  # ── 913-F6.  A TRANSLATED licence title is invisible to a title-line grader, and that is the
  # cost of 913-F1's fix: the body-grep it replaced would have caught "AFFERO" in any language.
  # `portabilis/i-diario` is AGPL-3.0 titled "LICENCA PUBLICA GERAL AFFERO GNU" (with cedilla and
  # acute accents); p913's first cut graded it UNKNOWN-TEMPLATE while the SHELF HAD IT RIGHT.
  # This base's `T20`/`T29` record vernacular supply as a measured phenomenon, so translated
  # grants are the predictable blind spot of a title-line instrument.
  #
  # 🔴 AND THE FIRST FIX FOR IT WAS A SILENT NO-OP, for a reason worth committing: this container
  # runs `LC_CTYPE=POSIX`, under which `tr '[:upper:]' '[:lower:]'` LEAVES ACCENTED CAPITALS
  # UNTOUCHED — the title folds to "licenCa pUblica geral affero gnu".  A pattern written with
  # lowercase accented characters can therefore NEVER match, and it fails as a no-op rather than
  # as an error.  Every test below is keyed on ASCII-only tokens (`licen`, `affero`, `geral`,
  # `menor`), which do fold correctly under POSIX.
  # Gated on size: a translated licence TEXT is long (a translated GPL/AGPL is ~35 kB).  A SHORT
  # payload that merely names a licence is a reference, not a text, and belongs to the
  # BY-REFERENCE stage below, which keeps the version and says the text is not present — a
  # strictly better verdict.  Without this gate the stage shadowed it (`parmentelat/nbautoeval`,
  # 289 B, graded `CC-UNSPECIFIED` and losing the `-SA`).
  if [ "${#fam[@]}" -eq 0 ] && [ "$bytes" -ge 600 ] && printf '%s' "$t" | grep -qi 'licen'; then
    if   printf '%s' "$t" | grep -qi 'affero'; then
      fam=("AGPL-3.0"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    elif printf '%s' "$t" | grep -qiE 'lesser|menor|reducida|amoindrie'; then
      fam=("LGPL"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    elif printf '%s' "$t" | grep -qiE 'geral|generale|general'; then
      fam=("GPL"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    elif printf '%s' "$t" | grep -qiE 'creative common|comun creativ|comum criativ'; then
      fam=("CC-UNSPECIFIED"); note="TRANSLATED grant title, graded on ASCII tokens (913-F6)"
    fi
  fi

  # ── 921-F1.  920-G2 DISCHARGED: A NOTICE IS NOT A LICENCE TEXT, AND THE VERSION LIVES IN ITS
  # PROSE.  `konlpy/konlpy` (722 B, `sha256_12 a66980ac3c64`) carries the GPL *notice* — the
  # paragraph upstream pastes into a file header — not the licence body.  The title line names
  # "GNU General Public License", so the primary rule returns a bare `GPL` with NO VERSION, and
  # `GPL-2.0-only` and `GPL-3.0-or-later` are not interchangeable for a client build: the first
  # is incompatible with Apache-2.0 and the second is not.  The version exists only in the prose
  # ("either version 3 of the License, or (at your option) any later version"), so where the
  # family is a GNU one and the payload is too small to BE the licence text (the real bodies are
  # ~18-35 kB), fall through to a version regex over the body.  A payload that carries the full
  # text keeps its family unqualified, because there the version is structural, not prose.
  # ── 921-F4.  A RESIDUAL OF THE SAME CLASS, FOUND BY RUNNING 921-F1's OWN FIX AT SCALE, AND IT
  # IS NOT CONFINED TO SHORT PAYLOADS.  `bretttolbert/verbecc` byte-reads 7,652 B whose title
  # block is "GNU LESSER GENERAL PUBLIC LICENSE / Version 3, 29 June 2007" — the version is
  # RIGHT THERE, on the second line of the block this grader already reads — and the primary rule
  # still returned a bare `LGPL`, because the `case` extracts a FAMILY and never a version.
  # 920-G2 was written as if the defect were a property of notice-style payloads; it is a
  # property of the grader.  LGPL-2.1 and LGPL-3.0 differ for a client build, so the version is
  # extracted from the title block at EVERY size.  🔵 What is NOT claimed: the "or later"
  # election lives in the program's own notice, not in the licence text, so a full text yields a
  # bare version (`LGPL-3.0`) and never an `-or-later` suffix.  That is why this stage runs
  # BEFORE 921-F1's and leaves short payloads to it.  Control: `vngrs-ai/vnlp`, 34,523 B stock
  # AGPL-3.0 (`sha256_12 8486a10c4393`), which already carries its version in the family.
  # ── 922-F3.  921-F4 FIXED THE WRONG AXIS, FOR THE THIRD TIME ON ONE DEFECT.
  # `920-G2` framed the version-dropping defect as a property of SHORT payloads.  `921-F4`
  # refuted that, reframed it as a property of the grader "at EVERY size", and fixed it — inside
  # `case "${fam[0]}" in GPL|LGPL)`.  The axis is neither size nor the grader in general: it is
  # the FAMILY ALLOW-LIST.  Measured p922 on `ufal/udpipe`, the only artefact carrying the Czech
  # substrate tier: a 16,725 B payload whose first line is "Mozilla Public License Version 2.0"
  # was published as a bare `MPL`.  🔵 MPL-1.1 and MPL-2.0 are NOT interchangeable — 1.1 is
  # GPL-INCOMPATIBLE and 2.0 is compatible by construction (s.3.3), which is the whole question
  # a delivery team asks of an MPL row.  The transferable rule, and it is 913-F2's lesson again:
  # A FIX SCOPED BY AN ALLOW-LIST IS A FIX THAT WILL BE WRONG ON THE NEXT FAMILY ENCOUNTERED.
  # ── 923-F2.  THE ALLOW-LIST IS REPLACED BY A TABLE, AND THE TABLE IS THE WHOLE RULE.
  # `922-G2` asked for this and predicted the live defect would be Apache-1.1 published as 2.0.
  # 🔴 It is not: `923-F1` measured Apache-1.1 and Apache-1.0 as **`BSD / BODY-BSD`** — the
  # version stage was never reached, because the FAMILY detector is keyed on `apache license`,
  # a string the ASF only adopted at 2.0.  Four framings of one defect, each correcting the
  # last and each still naming the wrong axis: size (`920-G2`) → the grader (`921-F4`) → the
  # version stage's allow-list (`922-F3`) → the family detector itself (`923-F1`).
  # 🔵 THE TRANSFERABLE RULE: a detector keyed on a product's CURRENT name cannot see that
  # product's EARLIER names, and a version stage cannot be wrong about a family it is never
  # handed.  So the version read is now driven by one table covering every family that has more
  # than one published version.  A family whose root is in the table and whose version is NOT
  # recoverable stays a BARE ROOT and says so — `922-F3`'s MPL precedent, generalised.
  VERSIONED_ROOTS="Apache MPL GPL LGPL AGPL ECL EPL CDDL MulanPSL MulanPubL CC-BY CC-BY-SA CC-BY-NC CC-BY-ND CC-BY-NC-SA CC-BY-NC-ND"
  # root<TAB>regex<TAB>version, specific before generic, first match wins.
  VERSION_TABLE=$(cat <<'VT'
Apache	version 2\.0	2.0
Apache	version 1\.1	1.1
Apache	version 1\.0	1.0
MPL	version 2\.0	2.0
MPL	version 1\.1	1.1
MPL	version 1\.0	1.0
GPL	version 3	3.0
GPL	version 2\.1	2.1
GPL	version 2	2.0
LGPL	version 3	3.0
LGPL	version 2\.1	2.1
LGPL	version 2	2.0
AGPL	version 3	3.0
AGPL	version 1	1.0
ECL	version 2\.0	2.0
ECL	version 1\.0	1.0
EPL	version 2\.0	2.0
EPL	version 1\.0	1.0
CDDL	version 1\.1	1.1
CDDL	version 1\.0	1.0
MulanPSL	第2版|version 2	2.0
MulanPSL	第1版|version 1	1.0
MulanPubL	第2版|version 2	2.0
MulanPubL	第1版|version 1	1.0
CC-BY	4\.0	4.0
CC-BY	3\.0	3.0
CC-BY	2\.5	2.5
CC-BY	2\.0	2.0
CC-BY	1\.0	1.0
CC-BY-SA	4\.0	4.0
CC-BY-SA	3\.0	3.0
CC-BY-SA	2\.5	2.5
CC-BY-SA	2\.0	2.0
CC-BY-SA	1\.0	1.0
CC-BY-NC	4\.0	4.0
CC-BY-NC	3\.0	3.0
CC-BY-NC	2\.5	2.5
CC-BY-NC	2\.0	2.0
CC-BY-NC	1\.0	1.0
CC-BY-ND	4\.0	4.0
CC-BY-ND	3\.0	3.0
CC-BY-ND	2\.5	2.5
CC-BY-ND	2\.0	2.0
CC-BY-ND	1\.0	1.0
CC-BY-NC-SA	4\.0	4.0
CC-BY-NC-SA	3\.0	3.0
CC-BY-NC-SA	2\.5	2.5
CC-BY-NC-SA	2\.0	2.0
CC-BY-NC-SA	1\.0	1.0
CC-BY-NC-ND	4\.0	4.0
CC-BY-NC-ND	3\.0	3.0
CC-BY-NC-ND	2\.5	2.5
CC-BY-NC-ND	2\.0	2.0
CC-BY-NC-ND	1\.0	1.0
VT
)
  if [ "${#fam[@]}" -gt 0 ] && [ "$bytes" -ge 1500 ]; then
    local root="${fam[0]}" rver=""
    case " $VERSIONED_ROOTS " in
      *" $root "*)
        while IFS=$'\t' read -r vr vx vv; do
          [ "$vr" = "$root" ] || continue
          printf '%s' "$t" | grep -qiE "$vx" && { rver="$vv"; break; }
        done <<< "$VERSION_TABLE"
        if [ -n "$rver" ]; then
          fam[0]="${root}-${rver}"
          case "$root" in
            GPL|LGPL|AGPL) note="version read from the title block (921-F4/923-F2); the \"or later\" election is NOT in the licence text — read the program's own notice" ;;
            MPL)    note="version read from the title block (922-F3/923-F2); MPL-1.1 is GPL-incompatible and MPL-2.0 is not" ;;
            Apache) note="version read from the title block (923-F2); Apache-1.0 and 1.1 are GPL-INCOMPATIBLE and carry NO patent grant — only 2.0 does" ;;
            *)      note="version read from the title block (923-F2)" ;;
          esac
        else
          # ── 923-F3.  APACHE-1.0 HAS NO LICENCE TITLE AT ALL — only `Copyright (c) 1995-1999 The
          # Apache Group`.  There is no version to read, so the discriminator has to be STRUCTURAL:
          # clause 3 of 1.0 is the ADVERTISING clause ("All advertising materials mentioning
          # features or use"), which 1.1 removed and replaced with a documentation acknowledgment.
          # That clause is also what makes it BSD-4-Clause-shaped, i.e. GPL-INCOMPATIBLE.
          if [ "$root" = "Apache" ] && grep -qiE 'all advertising materials mentioning features' "$B"; then
            fam[0]="Apache-1.0"
            note="no version in the title; graded 1.0 STRUCTURALLY on the advertising clause (923-F3) — BSD-4-Clause-shaped, GPL-INCOMPATIBLE, no patent grant"
          else
            note="${root} family with NO recoverable version in the title block — do not assume the current one (922-F3/923-F2)"
          fi
        fi ;;
    esac
  fi

  if [ "${#fam[@]}" -gt 0 ] && [ "$bytes" -lt 1500 ]; then
    # 923-F2: this stage keyed on `AGPL-3.0`, the versioned string the title case used to emit.
    # Once the title case emitted the ROOT, a notice-style Affero payload stopped reaching it.
    case "${fam[0]}" in
      GPL|LGPL|AGPL)
        local vnum="" vtail=""
        if   grep -qiE 'version 3[^0-9]' "$B"; then vnum="3.0"
        elif grep -qiE 'version 2\.1' "$B";   then vnum="2.1"
        elif grep -qiE 'version 2[^0-9]' "$B"; then vnum="2.0"; fi
        if [ -n "$vnum" ]; then
          if grep -qiE 'any later version' "$B"; then vtail="-or-later"; else vtail="-only"; fi
          fam[0]="${fam[0]}-${vnum}${vtail}"
          note="NOTICE-STYLE payload (${bytes} B) — family from the title line, VERSION recovered from the prose (921-F1 / 920-G2)"
        else
          note="NOTICE-STYLE payload (${bytes} B) naming a GNU family with NO recoverable version — do not assume 3.0 (921-F1)"
        fi ;;
    esac
  fi

  if [ "${#fam[@]}" -gt 0 ]; then
    v="${fam[0]}"
    # p640's MIT size band, applied to a TITLE-matched MIT too.
    if [ "$v" = "MIT" ] && { [ "$bytes" -lt 1000 ] || [ "$bytes" -gt 1250 ]; }; then
      v="MIT-TITLE-OUT-OF-BAND"; note="MIT title at ${bytes} B, outside the 1000-1250 B MIT band — read the modifications"
    fi
    # a second LIVE family in the body of a title-graded payload is still a conjunctive obligation
    # 913-F3: a title names ONE licence; a payload may still carry others.  p880's control
    # (apereo/java-cas-client = Apache-2.0 notice + a separate JA-SIG BSD-3-Clause grant) is
    # the reason this runs for EVERY title-graded family, not just the GNU ones.
    local extra=() head_fam="${fam[0]}"
    # ── 922-F4.  THE CONJUNCTIVE DEDUP COMPARED THE VERSIONED STRING, NOT THE FAMILY.  Found by
    # running 922-F3's own fix: once the title read `MPL-2.0`, `[ "$head_fam" != "MPL" ]` stopped
    # matching and the SAME licence was re-detected in the body as a second grant — `ufal/udpipe`
    # published as `MPL-2.0+MPL / CONJUNCTIVE`, a two-licence notice obligation that does not
    # exist.  🔵 This is 921-F4's own lesson paying out twice in one pass: a fix is run over the
    # cohort before it is believed, AND its interaction with every later stage is re-controlled.
    local head_root="${head_fam%%-[0-9]*}"
    [ "$head_root" != "Apache" ] && grep -qi "apache license" "$B" && extra+=("Apache-2.0")
    [ "$head_root" != "MIT" ] && [ "$head_root" != "BSL" ] \
      && grep -q "Permission is hereby granted, free of charge" "$B" && extra+=("MIT")
    # ── 923-F4.  THE 922-F4 CLASS, REPRODUCED BY THIS PASS'S OWN FIX AND CAUGHT BY ITS OWN
    # CONTROLS.  Once `923-F1` made Apache-1.1 reachable, the BSD probe below fired on its body
    # and it published as `Apache-1.1+BSD / CONJUNCTIVE` — a two-licence notice obligation that
    # does not exist.  Apache-1.0/1.1 are BSD-PHRASED BY CONSTRUCTION ("Redistribution and use in
    # source and binary forms" is clause 1 of the Apache text itself), so for those two versions
    # the BSD hit is the SAME grant, not a second one.  Apache-2.0 is not BSD-phrased, so it is
    # deliberately NOT exempted here.  🔵 `921-F4`'s prescription paying out a third time: a fix
    # is re-controlled against every stage DOWNSTREAM of it, not only the cohort it came from.
    local ap1x=0; case "$head_fam" in Apache-1.0|Apache-1.1) ap1x=1 ;; esac
    [ "$head_root" != "BSD" ] && [ "$ap1x" -eq 0 ] \
      && grep -qi "Redistribution and use in source and binary" "$B" && extra+=("BSD")
    [ "$head_root" != "MPL" ] && grep -qi "mozilla public license" "$B" && extra+=("MPL")
    case "$head_fam" in CC-*|CC0-*) : ;; *)
      grep -qi "creative commons" "$B" && extra+=("CC-UNSPECIFIED") ;; esac
    if [ "${#extra[@]}" -gt 0 ]; then
      fam+=("${extra[@]}"); v="CONJUNCTIVE"
      note="title grants ${fam[0]} and the body carries ${#extra[@]} further family/families — notice obligation of ${#fam[@]}"
    fi
    case "$v" in CC-*|CC0-*) note="${note:+$note; }Creative Commons grant — content licence, read scope before building on it" ;; esac
    printf '%s\t%s\t%s\n' "$(IFS=+; echo "${fam[*]}")" "$v" "$note"; return
  fi

  # ---- FALLBACK: no licence title. ----
  # 913-F8, three classes of payload that NAME a grant without reproducing it.  All three were
  # graded UNKNOWN-TEMPLATE by p913's first cut and in two of the three the SHELF WAS RIGHT, so
  # "unknown" would have destroyed a correct cell.
  #   (a) MANIFEST-DEFERRED — the R convention: `DESCRIPTION` says `License: MIT + file LICENSE`
  #       and LICENSE carries only YEAR and COPYRIGHT HOLDER (`LJKelly3141/coursepack`, 41 B).
  #       The grant is in the PACKAGE MANIFEST, which is the axis gate `905-G1` already watches.
  #   (b) BY-REFERENCE — the payload cites a licence and a URL instead of reproducing the text
  #       (`parmentelat/nbautoeval`, 289 B, "Creative Common Licence CC BY-SA 4.0" — note the
  #       singular "Common", which a `Creative Commons` grep misses by one letter).
  #   (c) SPLIT-BY-ASSET-TYPE — one repository, two grants, divided by what the asset IS
  #       (`bncc-dev/bncc-benchmark`: "Código — MIT" for code, another grant for content).  This
  #       is `T25` and gate `904-G1` in a single payload, declared in prose and in Portuguese.
  if [ "$bytes" -lt 120 ] && grep -qiE "copyright holder|titular" "$B" \
     && ! grep -qiE "permission|redistribution|warranty" "$B"; then
    printf 'none	MANIFEST-DEFERRED	%s B carrying only a copyright holder and year — the grant is declared in the PACKAGE MANIFEST (R: DESCRIPTION `License:`), not here.  Read the manifest (905-G1); do NOT read this as ungranted
' "$bytes"; return
  fi
  # locale-safe: ASCII tokens only, for the reason given in 913-F6.
  if [ "$bytes" -lt 4000 ] && grep -qiE '(^|[^A-Za-z])MIT([^A-Za-z]|$)' "$B" \
     && grep -qiE 'CC[ -]?BY' "$B"; then
    local sfam="MIT(code)"
    if grep -qiE 'CC[ -]?BY[ -]?SA' "$B"; then sfam="$sfam+CC-BY-SA(content)"
    else sfam="$sfam+CC-BY(content)"; fi
    printf '%s\tSPLIT-BY-ASSET-TYPE\tone repository, two grants divided by ASSET TYPE and declared in prose (%s B) — a single licence cell cannot express it, and the permissive half is the CODE while the data/content half is attribution- or share-alike-bound (T25, gate 904-G1)\n' "$sfam" "$bytes"; return
  fi
  if [ "$bytes" -lt 600 ]; then
    local rfam=""
    grep -qiE "CC[ -]?BY[ -]?SA" "$B" && rfam="CC-BY-SA"
    [ -z "$rfam" ] && grep -qiE "CC[ -]?BY[ -]?NC" "$B" && rfam="CC-BY-NC"
    [ -z "$rfam" ] && grep -qiE "CC0" "$B" && rfam="CC0-1.0"
    [ -z "$rfam" ] && grep -qiE "CC[ -]?BY\b" "$B" && rfam="CC-BY"
    [ -z "$rfam" ] && grep -qiE "creative common" "$B" && rfam="CC-UNSPECIFIED"
    [ -z "$rfam" ] && grep -qiE "\bMIT\b" "$B" && rfam="MIT"
    [ -z "$rfam" ] && grep -qiE "apache" "$B" && rfam="Apache-2.0"
    [ -z "$rfam" ] && grep -qiE "\bAGPL\b" "$B" && rfam="AGPL-3.0"
    [ -z "$rfam" ] && grep -qiE "\bGPL\b" "$B" && rfam="GPL"
    if [ -n "$rfam" ]; then
      printf '%s	BY-REFERENCE-%s	the grant is NAMED and linked, not reproduced (%s B) — binding, but the scope cannot be read from this repository; fetch the referenced text before relying on it
' "$rfam" "$rfam" "$bytes"; return
    fi
  fi
  local bfam=() boost=0
  grep -qi "Boost Software License" "$B" && { bfam+=("BSL-1.0"); boost=1; }
  grep -qi "Apache License, Version 2.0\|Apache License\b" "$B" && bfam+=("Apache-2.0")   # 923-F2: body probe sees only the 2.0 name
  [ "$boost" -eq 0 ] && grep -q "Permission is hereby granted, free of charge" "$B" && bfam+=("MIT")
  # ── 923-F3.  APACHE-1.0 CARRIES NO LICENCE TITLE AT ALL — its payload opens
  # `Copyright (c) 1995-1999 The Apache Group.  All rights reserved.`  There is nothing for a
  # title-line grader to match, so `923-F1`'s family fix cannot reach it and it was still
  # published as `BSD / BODY-BSD`.  The only available discriminator is STRUCTURAL: clause 3
  # of Apache-1.0 is the ADVERTISING clause, which 1.1 removed and replaced with a
  # documentation acknowledgment, and which is also what makes 1.0 BSD-4-Clause-shaped and
  # therefore GPL-INCOMPATIBLE.  A bare `BSD` cell is read as BSD-3-Clause, which is
  # GPL-COMPATIBLE — so the misgrade ran in the PERMISSIVE direction, which is the direction
  # that loses a client an argument it cannot win back.  Requires BOTH the clause and the
  # Apache attribution string, so a generic BSD-4-Clause payload is not captured.
  if grep -qiE "all advertising materials mentioning features" "$B" \
     && grep -qiE "the apache group|apache software foundation" "$B"; then
    bfam+=("Apache-1.0")
    note="${note:+$note; }no licence title; graded Apache-1.0 STRUCTURALLY on the advertising clause + ASF attribution (923-F3) — BSD-4-Clause-shaped, GPL-INCOMPATIBLE, no patent grant"
  else
    grep -qi "Redistribution and use in source and binary" "$B" && bfam+=("BSD")
  fi
  # 913-F1: in the body the GNU families are decided by COUNT, never by presence.
  if grep -qi "general public license" "$B"; then
    local na; na=$(grep -oic "affero" "$B")
    if   [ "$na" -ge 10 ]; then bfam+=("AGPL-3.0")
    elif grep -qi "GNU LESSER GENERAL PUBLIC LICENSE" "$B"; then bfam+=("LGPL")
    else bfam+=("GPL"); note="GNU family graded from the body: ${na} Affero mention(s) — GPL-3.0 s.13 names Affero 3x"
    fi
  fi
  grep -qi "Mozilla Public License" "$B" && bfam+=("MPL")
  grep -qiE "木兰宽松许可证|mulan permissive software license" "$B" && bfam+=("MulanPSL-2.0")
  grep -qiE "木兰公共许可证|mulan public license" "$B" && bfam+=("MulanPubL-2.0")
  if   grep -qi "CC0 1.0 Universal" "$B"; then bfam+=("CC0-1.0")
  elif grep -qi "Creative Commons Attribution-ShareAlike" "$B"; then bfam+=("CC-BY-SA")
  elif grep -qi "Creative Commons Attribution-NonCommercial" "$B"; then bfam+=("CC-BY-NC")
  elif grep -qi "Creative Commons Attribution" "$B"; then bfam+=("CC-BY")
  elif grep -qiE "Creative Commons?" "$B"; then bfam+=("CC-UNSPECIFIED"); fi
  # ── 918-F1.  THE NONCOMMERCIAL MATCHER FIRED ON STOCK GNU TEXT. ──
  # This line was an unguarded substring match over the WHOLE body, and it is reachable only from
  # the title-less FALLBACK branch.  Every GPL-3.0 and AGPL-3.0 payload contains, in section 6:
  #     "alternative is allowed only occasionally and noncommercially, and"
  # so ANY title-less payload that embeds GNU text was given a spurious NONCOMMERCIAL-TERM family.
  # Measured on `PrairieLearn/PrairieLearn` (LICENSE@master, 37,237 B, no licence title line): the
  # true grant is MIT + AGPL-3.0, a notice obligation of 2, and p918 first read it as
  # BODY-CONJUNCTIVE over THREE families with a NONCOMMERCIAL term that does not exist.  Publishing
  # that would have told a studio the strongest open STEM assessment engine carries a
  # noncommercial restriction -- an error in the direction that KILLS a deliverable build.
  # 913-F2's lesson applies: the guard lives in the authority, not in a caller.
  if grep -qi "non-commercial\|noncommercial" "$B" \
     && ! grep -qi "allowed only occasionally and noncommercially" "$B"; then
    bfam+=("NONCOMMERCIAL-TERM")
  fi

  if [ "${#bfam[@]}" -eq 0 ]; then
    v="UNKNOWN-TEMPLATE"
    if [ "$bytes" -lt 200 ] && grep -qiE "GPL|MIT|Apache|BSD" "$B"; then
      v="DECLARATION-ONLY"
      note="${bytes} B, names a licence but carries NO licence text: $(tr -d '\n' < "$B" | cut -c1-60)"
    else
      note="no licence title and no grant phrase; title block was: $(printf '%s' "$title" | cut -c1-60)"
    fi
  elif [ "${#bfam[@]}" -eq 1 ]; then v="BODY-${bfam[0]}"
    note="${note:+$note; }graded from the body, not a licence title — weaker evidence than a title verdict"
  else v="BODY-CONJUNCTIVE"
    note="${note:+$note; }${#bfam[@]} families in the body, no licence title — notice obligation of ${#bfam[@]}"
  fi
  printf '%s\t%s\t%s\n' "$(IFS=+; echo "${bfam[*]:-none}")" "$v" "$note"
}

printf 'repo\tbranch\tpath\thttp\tbytes\tsha256_12\tfamilies\tverdict\tnote\n' > "$OUT"

emit() {  # $1=slug $2=branch $3=path  (branch/path known -> no API call)
  local slug="$1" br="$2" f="$3" code bytes m res
  code=$(curl -sS --max-time 30 -o "$D/x" -w '%{http_code}' \
         "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
  if [ "$code" != "200" ]; then
    printf '%s\t%s\t%s\t%s\t0\t-\tnone\tPAYLOAD-GONE\twas readable when the input TSV was made\n' \
      "$slug" "$br" "$f" "$code" >> "$OUT"; return
  fi
  bytes=$(wc -c < "$D/x" | tr -d ' '); m=$(sha256sum "$D/x" | cut -c1-12)
  res=$(adjudicate "$D/x" "$bytes")
  # 913-F4: dual-grant detection.  A repository carrying BOTH LICENSE-MIT and LICENSE-APACHE is
  # offered under EITHER (the Rust convention); reporting one of the two is a half-truth, and the
  # obligation a client inherits is the one they CHOOSE, not the one the filename list hit first.
  case "$f" in
    LICENSE-MIT|LICENSE-APACHE)
      local o oc
      [ "$f" = "LICENSE-MIT" ] && o="LICENSE-APACHE" || o="LICENSE-MIT"
      oc=$(curl -sS --max-time 20 -o /dev/null -w '%{http_code}' \
           "https://raw.githubusercontent.com/$slug/$br/$o" 2>/dev/null)
      if [ "$oc" = "200" ]; then
        res=$(printf 'MIT+Apache-2.0\tDUAL-MIT-OR-Apache-2.0\tboth LICENSE-MIT and LICENSE-APACHE are present and readable — the licensee ELECTS one; this is a disjunctive offer, not a conjunctive obligation')
      fi ;;
  esac
  printf '%s\t%s\t%s\t200\t%s\t%s\t%s\n' "$slug" "$br" "$f" "$bytes" "$m" "$res" >> "$OUT"
}

if [ "$1" = "--from-tsv" ]; then
  # re-adjudicate rows already located by a previous instrument: branch+path are FACTS in the
  # input, so this path makes NO search-API call at all.
  tail -n +2 "$2" | while IFS=$'\t' read -r repo _db br path http _rest; do
    [ "$http" = "200" ] || { printf '%s\t%s\t%s\t%s\t0\t-\tnone\tNO-PAYLOAD-IN-INPUT\tcarried through from the input TSV\n' \
        "$repo" "${br:--}" "${path:--}" "$http" >> "$OUT"; continue; }
    emit "$repo" "$br" "$path"
  done
else
  for slug in "$@"; do
    db=$(gh api -X GET search/repositories -f q="repo:$slug" --jq '.items[0].default_branch // ""' 2>/dev/null); sleep 2
    branches=(); [ -n "$db" ] && branches+=("$db")
    for b in main master develop; do [ "$b" != "$db" ] && branches+=("$b"); done
    found=0
    for br in "${branches[@]}"; do for f in "${NAMES[@]}"; do
      code=$(curl -sS --max-time 30 -o "$D/p" -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
      [ "$code" = "200" ] || continue
      # ── 922-F2.  A POINTER IS NOT A PAYLOAD, AND THE PROBE STOPPED AT THE FIRST HTTP 200
      # RATHER THAN AT THE FIRST GRANT.  Measured p922 on `flammie/omorfi` (108 ★, the Finnish
      # open-morphology stack): `LICENSE` is SEVEN BYTES whose entire content is the string
      # `COPYING`, and `COPYING` is a 35,140 B GNU GPL-3.0 text.  The authority published
      # `none / UNKNOWN-TEMPLATE` for a repository with an unambiguous copyleft grant — a
      # FALSE-PERMISSIVE-ADJACENT read on the exact artefact class this instrument exists for.
      # 🔵 Every earlier grant fix in this file answers WHAT TO READ; this one answers WHEN TO
      # STOP.  Narrow by construction: fires only when the payload is under 64 B and its trimmed
      # content is itself one of the names already being probed.
      if [ "$(wc -c < "$D/p")" -lt 64 ]; then
        ptr=$(tr -d ' \t\r\n' < "$D/p")
        for n in "${NAMES[@]}" "${SIBLINGS[@]}"; do
          [ "$ptr" = "$n" ] || continue
          pc=$(curl -sS --max-time 30 -o "$D/p2" -w '%{http_code}' \
               "https://raw.githubusercontent.com/$slug/$br/$ptr" 2>/dev/null)
          if [ "$pc" = "200" ]; then mv "$D/p2" "$D/p"; f="$ptr"
            fi   # the emitted `path` column then shows the POINTED-TO file, which is the evidence
          break
        done
      fi
      emit "$slug" "$br" "$f"; found=1
      # 921-F2 / 920-G1: the primary payload is not necessarily the only grant.  Probe the named
      # asset-sibling list on the SAME branch and emit a row for EVERY one that resolves.  A repo
      # whose only grant is the plain file emits exactly one row — that is the false-positive
      # control, and `konlpy/konlpy` is the standing fixture for it.
      if [ "${SKIP_SIBLINGS:-0}" != "1" ]; then
        for sb in "${SIBLINGS[@]}"; do
          [ "$sb" = "$f" ] && continue
          sc=$(curl -sS --max-time 15 -o /dev/null -w '%{http_code}' \
               "https://raw.githubusercontent.com/$slug/$br/$sb" 2>/dev/null)
          [ "$sc" = "200" ] && emit "$slug" "$br" "$sb"
        done
      fi
      break 2
    done; done
    [ $found -eq 0 ] && printf '%s\t-\t-\t404\t0\t-\tnone\tNO-LICENCE-FILE-FOUND\tsearched %d names over %d branches\n' \
      "$slug" "${#NAMES[@]}" "${#branches[@]}" >> "$OUT"
  done
fi
