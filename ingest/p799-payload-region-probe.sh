#!/usr/bin/env bash
# p799 instrument: payload-based region provenance + readme-vs-payload + cell-shape assertion.
# Channel: blobless clone (p796-F), because curl -sI is 403 for live AND invented addresses (T923)
# and repos/{owner}/{repo} is refused in a repo-scoped session (T941).
# Writes TSV. Every cell shape-asserted before it is emitted (ACTION p798-E).
set -u
WORK="${WORK:-/tmp/claude-0/-home-user-globant-kb/32a97be9-4b3c-5665-918f-44e3ee7ca9a2/scratchpad/p799/clones}"
mkdir -p "$WORK"

# --- p798-E: shape gates. A cell that fails its declared kind is emitted as NA_<reason>, never raw.
shape_sha(){ [[ "$1" =~ ^[0-9a-f]{12,40}$ ]] && echo "$1" || echo "NA_shape"; }
shape_int(){ [[ "$1" =~ ^[0-9]+$ ]] && echo "$1" || echo "NA_shape"; }
shape_date(){ [[ "$1" =~ ^[0-9]{4}-[0-9]{2}-[0-9]{2}$ ]] && echo "$1" || echo "NA_shape"; }
shape_text(){ local v="$1"
  case "$v" in *'{"message"'*) echo "NA_refused_api"; return;; esac   # T941 defect class
  v="${v//$'\t'/ }"; v="${v//$'\n'/ }"; [ -z "$v" ] && v="NA_empty"; echo "$v"; }

printf 'address\thead_commit\tlicence_file\tlicence_blob\tlicence_bytes\tgrant\tstars\tlast_push\tregion_signal\tregion_verdict\treadme_restriction\n'

for ADDR in "$@"; do
  OWNER="${ADDR%%/*}"; NAME="${ADDR##*/}"; D="$WORK/${OWNER}__${NAME}"
  rm -rf "$D"
  if ! git clone --filter=blob:none --no-checkout --depth 1 -q "https://github.com/$ADDR" "$D" 2>/dev/null; then
    printf '%s\tNA_clone_failed\tNA\tNA\tNA\tNA_clone_failed\tNA\tNA\tNA\tNA_unresolved\tNA\n' "$ADDR"; continue
  fi
  HEAD_SHA=$(shape_sha "$(git -C "$D" rev-parse HEAD 2>/dev/null | cut -c1-12)")
  TREE=$(git -C "$D" ls-tree -l HEAD 2>/dev/null)

  # --- licence payload, byte-verified
  LFILE="NA"; LBLOB="NA"; LBYTES="NA"; GRANT="NA_no_licence_file"
  LROW=$(echo "$TREE" | awk '$2=="blob" && $5 ~ /^(LICENSE|LICENCE|COPYING|LICENSE\.md|LICENSE\.txt|LICENCE\.md|COPYING\.txt|LICENSE-MIT|LICENSE-APACHE)$/' | head -1)
  if [ -n "$LROW" ]; then
    LFILE=$(echo "$LROW" | awk '{print $5}'); LBLOB=$(shape_sha "$(echo "$LROW" | awk '{print $3}' | cut -c1-12)")
    LBYTES=$(shape_int "$(echo "$LROW" | awk '{print $4+0}')")
    BODY=$(git -C "$D" cat-file blob "$(echo "$LROW" | awk '{print $3}')" 2>/dev/null)
    # T942: classify on the TITLE (first 5 lines). GPL-3.0 section 13 NAMES the AGPL,
    # so any body-substring grader misreads GPL-3.0 as AGPL-3.0.
    HEADTXT=$(echo "$BODY" | head -5)
    if   echo "$HEADTXT" | grep -qi 'Apache License'; then GRANT="Apache-2.0"
    elif echo "$HEADTXT" | grep -qi 'MIT License'; then GRANT="MIT"
    elif echo "$BODY" | grep -qi 'Permission is hereby granted, free of charge'; then GRANT="MIT_noheader"
    elif echo "$HEADTXT" | grep -qi 'GNU AFFERO'; then GRANT="AGPL-3.0"
    elif echo "$HEADTXT" | grep -qi 'GNU GENERAL PUBLIC'; then GRANT="GPL"
    elif echo "$BODY" | grep -qi 'GNU LESSER'; then GRANT="LGPL"
    elif echo "$BODY" | grep -qi 'BSD'; then GRANT="BSD"
    elif echo "$BODY" | grep -qi 'Mozilla Public'; then GRANT="MPL-2.0"
    else GRANT="OTHER_unclassified"; fi
  fi

  # --- metadata channel first: search/* is the only one open here (T941), and the repository
  # DESCRIPTION it returns is a SIXTH origin channel that resolves rows the payload does not (T946).
  J=$(gh api -X GET search/repositories -f q="repo:$ADDR" -f per_page=1 2>/dev/null)
  DESC=$(printf '%s' "$J" | python3 -I -c 'import sys,json
try:
  d=json.load(sys.stdin); i=(d.get("items") or [{}])[0]; print(i.get("description") or "")
except Exception: print("")' 2>/dev/null)

  # --- region provenance from PAYLOAD, not from query language (ACTION p798-A)
  SIG="NA_none"; VERDICT="unresolved"
  DOCS="$DESC"
  for P in README.md README.rst README.txt readme.md NOTICE NOTICE.md NOTICE.txt docs/README.md; do
    B=$(echo "$TREE" | awk -v p="$P" '$2=="blob" && $5==p {print $3}' | head -1)
    [ -n "$B" ] && DOCS="$DOCS
$(git -C "$D" cat-file blob "$B" 2>/dev/null | head -c 60000)"
  done
  if [ -n "$DOCS" ]; then
    # T943: acronym region-tokens are SUBSTRINGS of ordinary words. Brazil's ENEM sits inside the
    # Spanish "tenemos"; Brazil's INEP sits inside camelCase "...lineP...". So acronyms are matched
    # CASE-SENSITIVELY with word boundaries, and country/ccTLD evidence is kept in its own class.
    # T945: a bare COUNTRY NAME in a README is not origin evidence. i18n locale lists name
    # countries ("Portuguese (Brazil), Spanish (Mexico)"), so locale/language lines are removed
    # before the country scan. Strong signals (ministry acronym, ccTLD host, institution,
    # subnational territory) are read from the full payload.
    DOCS_NOI18N=$(printf '%s' "$DOCS" | grep -viE 'i18n|locale|localisation|localization|語|语言|supports? [0-9]+ (locales|languages)|Portuguese \(|Spanish \(|translat')
    ACR=$(printf '%s' "$DOCS" | grep -ohE '\b(ENEM|INEP|UNAM|MPPE|MINEDU|MINEDUC|SENCE|CONICET|SEP|INET|KHDA|MEXT)\b' | sort -u | paste -sd';' -)
    CTRY=$(printf '%s' "$DOCS_NOI18N" | grep -ohiE '\b(venezuela|peru|perú|colombia|chile|m[ée]xico|mexico|argentina|brasil|brazil|uruguay|bolivia|ecuador|paraguay|guatemala|rep[uu]blica dominicana|espa[nñ]a|spain|portugal)\b|perú|méxico|españa' | tr 'A-Z' 'a-z' | sort -u | paste -sd';' -)
    # T944: a BARE ccTLD is unsafe against any document containing file paths. Paraguay's .py is the
    # Python extension; .cl is Chile and OpenCL; .es is Spain and ECMAScript; .do, .ar, .pl likewise.
    # A ccTLD is therefore only accepted inside a URL HOST.
    TLD=$(printf '%s' "$DOCS" | grep -ohE 'https?://[A-Za-z0-9.-]+' | sed 's#https\?://##' | grep -oiE '\.(gob|gov|edu|ac|com|org|net)?\.?(ve|mx|ar|cl|pe|br|uy|bo|ec|py|do|gt|cr|es|pt)$' | tr 'A-Z' 'a-z' | sort -u | head -6 | paste -sd';' -)
    INST=$(printf '%s' "$DOCS" | grep -ohiE '(universidad[a-z]*|universitat|universidade|tecnol[óo]gico de monterrey|polit[ée]cnica de madrid|generalitat|xunta|junta de andaluc[íi]a|ceibal|erasmus|horizon europe|unirv|pivic|uni[a-z]{2,8}\\b)' | tr 'A-Z' 'a-z' | sort -u | head -6 | paste -sd';' -)
    # Subnational territories: a curriculum document naming an autonomous community is strong
    # EMEA evidence even with no ccTLD and no country word. Kept in its own class, and deliberately
    # excludes names shared across regions (e.g. Valencia is also a city in Venezuela).
    SUB=$(printf '%s' "$DOCS" | grep -ohiE '\b(comunidad de madrid|galicia|andaluc[íi]a|catalu[ñn]a|castilla|euskadi|extremadura|navarra|canarias|baleares|arag[óo]n)\b' | tr 'A-Z' 'a-z' | sort -u | head -4 | paste -sd';' -)
    AP=$(printf '%s' "$DOCS" | grep -ohiE '(tsinghua|peking university|zhejiang university|fudan|beihang|shanghai jiao|清华|北京大学|KAIST|\bNUS\b|Nanyang Technological|\bIIT [A-Z]|MEXT|\bTHU-)' | tr 'A-Z' 'a-z' | sort -u | head -4 | paste -sd';' -)
    SIG=$(shape_text "acr=[$ACR] ctry=[$CTRY] tld=[$TLD] inst=[$INST] sub=[$SUB] apac=[$AP]")

    # Verdict carries the TOKEN that produced it, so the grade is re-derivable from the bytes
    # beside it (p796-H / p797-C). EMEA is tested FIRST because the es-leg trap is Spain (T935).
    EM=$(printf '%s' "$CTRY;$TLD;$INST;$SUB" | grep -ohiE '\b(espa[nñ]a|spain|portugal)\b|\.(es|pt)\b|polit[ée]cnica de madrid|universitat|generalitat|xunta|junta de andaluc[íi]a|erasmus|horizon europe|\b(comunidad de madrid|galicia|andaluc[íi]a|catalu[ñn]a|castilla|euskadi|extremadura|navarra|canarias|baleares|arag[óo]n)\b' | head -1)
    LA=$(printf '%s' "$CTRY;$TLD;$INST;$ACR" | grep -ohE '\b(venezuela|peru|perú|colombia|chile|m[ée]xico|mexico|argentina|brasil|brazil|uruguay|bolivia|ecuador|paraguay|guatemala)\b|perú|méxico|\.(ve|mx|ar|cl|pe|br|uy|bo|ec|py|do|gt|cr)\b|\b(MPPE|MINEDU|MINEDUC|SENCE|CONICET|UNAM|INET|ENEM|INEP)\b|ceibal|universidade|tecnol[óo]gico de monterrey' | head -1)
    if   [ -n "$AP" ] && [ -z "$LA" ] && [ -z "$EM" ]; then VERDICT="APAC:${AP%%;*}"
    elif [ -n "$EM" ] && [ -z "$LA" ]; then VERDICT="EMEA:$EM"
    elif [ -n "$LA" ] && [ -z "$EM" ]; then VERDICT="LATAM:$LA"
    elif [ -n "$EM" ] && [ -n "$LA" ];  then VERDICT="CONFLICT:EMEA=$EM/LATAM=$LA"
    fi
  fi

  # --- readme-vs-payload: a restriction asserted in prose under a permissive grant (T937 / p798-B)
  RESTR="none"
  if [ -n "$DOCS" ]; then
    R=$(echo "$DOCS" | grep -ohiE '(do not remove[^.]{0,80}|must not be removed[^.]{0,60}|no comercial[^.]{0,60}|non-commercial use only|not for commercial use|may not be used commercially|attribution must[^.]{0,60}|keep[^.]{0,30}banner[^.]{0,40})' | head -3 | paste -sd' | ' -)
    [ -n "$R" ] && RESTR=$(shape_text "$R")
  fi
  case "$GRANT" in MIT|Apache-2.0|BSD|MPL-2.0) : ;; *) [ "$RESTR" != "none" ] && RESTR="$RESTR [copyleft_base]";; esac

  # --- recency + stars from search/* (already fetched above)
  STARS=$(shape_int "$(echo "$J" | python3 -I -c 'import sys,json
try:
  d=json.load(sys.stdin); i=d.get("items") or [{}]
  print(i[0].get("stargazers_count",""))
except Exception: print("")' 2>/dev/null)")
  PUSH=$(shape_date "$(echo "$J" | python3 -I -c 'import sys,json
try:
  d=json.load(sys.stdin); i=d.get("items") or [{}]
  print((i[0].get("pushed_at") or "")[:10])
except Exception: print("")' 2>/dev/null)")

  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$ADDR" "$HEAD_SHA" "$LFILE" "$LBLOB" "$LBYTES" "$GRANT" "$STARS" "$PUSH" "$SIG" "$VERDICT" "$RESTR"
done
