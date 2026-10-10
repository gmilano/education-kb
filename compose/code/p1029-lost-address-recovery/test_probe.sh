#!/usr/bin/env bash
# p1029 tests — offline, fixture-only. Exercises every pure function in
# classify.sh, including the orderings that a naive classifier gets wrong.
set -u
cd "$(dirname "$0")"
. ./classify.sh

PASS=0; FAIL=0
T=$(mktemp -d); trap 'rm -rf "$T"' EXIT

ok() { # ok <name> <expected> <actual>
  if [ "$2" = "$3" ]; then PASS=$((PASS+1)); printf 'ok   %s\n' "$1"
  else FAIL=$((FAIL+1)); printf 'FAIL %s — expected [%s] got [%s]\n' "$1" "$2" "$3"; fi
}

# 1 — MIT by its operative sentence, not by a filename or a title.
printf 'MIT License\n\nCopyright (c) 2019 Someone\n\nPermission is hereby granted, free of charge, to any person\n' > "$T/mit"
ok "1 MIT from operative sentence" "MIT" "$(classify_payload "$T/mit")"

# 2 — Apache-2.0 needs BOTH the name and the version.
printf '                                 Apache License\n                           Version 2.0, January 2004\n' > "$T/apache"
ok "2 Apache-2.0" "Apache-2.0" "$(classify_payload "$T/apache")"

# 3 — LGPL must NOT fall through to GPL. The LGPL text contains the string
#     "GNU GENERAL PUBLIC LICENSE" by reference, so order is the whole test.
printf 'GNU LESSER GENERAL PUBLIC LICENSE\nVersion 3, 29 June 2007\n\nThis version incorporates the terms and conditions of version 3 of the GNU GENERAL PUBLIC LICENSE.\n' > "$T/lgpl"
ok "3 LGPL not misread as GPL" "LGPL-3.0" "$(classify_payload "$T/lgpl")"

# 4 — AGPL likewise.
printf 'GNU AFFERO GENERAL PUBLIC LICENSE\nVersion 3, 19 November 2007\n...GNU GENERAL PUBLIC LICENSE...\n' > "$T/agpl"
ok "4 AGPL not misread as GPL" "AGPL-3.0" "$(classify_payload "$T/agpl")"

# 5 — BSD-3 vs BSD-2 turns on the third clause alone.
printf 'Redistribution and use in source and binary forms, with or without modification, are permitted.\n3. Neither the name of the copyright holder nor the names of its contributors\n' > "$T/bsd3"
ok "5a BSD-3-Clause" "BSD-3-Clause" "$(classify_payload "$T/bsd3")"
printf 'Redistribution and use in source and binary forms, with or without modification, are permitted.\n2. Redistributions in binary form must reproduce the above copyright notice.\n' > "$T/bsd2"
ok "5b BSD-2-Clause" "BSD-2-Clause" "$(classify_payload "$T/bsd2")"

# 6 — a zero-byte 200 is EMPTY, never a grant. A repo CAN serve an empty
#     LICENSE, and calling that "licensed" is the error this guards.
: > "$T/empty"
ok "6 empty payload is not a grant" "EMPTY" "$(classify_payload "$T/empty")"

# 7 — a non-licence file that happens to be served must not be classified.
printf '# Project\n\nInstall with pip.\n' > "$T/readme"
ok "7 README is UNRECOGNISED" "UNRECOGNISED" "$(classify_payload "$T/readme")"

# 8 — CRLF payloads classify the same as LF. GitHub serves both.
printf 'MIT License\r\n\r\nPermission is hereby granted, free of charge, to any person\r\n' > "$T/crlf"
ok "8 CRLF tolerated" "MIT" "$(classify_payload "$T/crlf")"

# 9 — CC is reported as its family, not as permissive. PERSUADE 2.0 is the
#     case that matters (CC-BY-NC-SA-4.0 looked open and was not).
printf 'Attribution-NonCommercial-ShareAlike 4.0 International\n\nCreative Commons Corporation is not a law firm.\n' > "$T/cc"
ok "9 CC family flagged" "CC-FAMILY" "$(classify_payload "$T/cc")"

# 10 — tag counting: peeled refs name the same tag as their parent.
cat > "$T/tags" <<'EOF'
aaa1	refs/tags/v1.0
aaa2	refs/tags/v1.0^{}
bbb1	refs/tags/v2.0
bbb2	refs/tags/v2.0^{}
ccc1	refs/tags/v3.0
EOF
ok "10 annotated tags counted once" "3" "$(count_tags "$T/tags")"

# 11 — no tags at all is 0, not an error and not blank.
: > "$T/notags"
ok "11 zero tags" "0" "$(count_tags "$T/notags")"

# 12 — a missing tags file degrades to 0 rather than failing the row.
ok "12 missing tags file" "0" "$(count_tags "$T/does-not-exist")"

# 13 — symref parsing.
cat > "$T/head" <<'EOF'
ref: refs/heads/master	HEAD
48c79a8f0e1d2c3b4a5968778899aabbccddeeff	HEAD
EOF
ok "13a head_ref" "master" "$(head_ref "$T/head")"
ok "13b head_sha" "48c79a8f0e1d2c3b4a5968778899aabbccddeeff" "$(head_sha "$T/head")"

# 14 — a repo with NO symref line (tag-only / detached HEAD) must still yield a
#     SHA, because that SHA is what the raw path falls back to.
cat > "$T/detached" <<'EOF'
1524a63f2bc53f6145ae94e3327b2b479fce0fcc	HEAD
EOF
ok "14a detached head_ref is -" "-" "$(head_ref "$T/detached")"
ok "14b detached head_sha survives" "1524a63f2bc53f6145ae94e3327b2b479fce0fcc" "$(head_sha "$T/detached")"

# 15 — HEAD must be read from the HEAD row, not from the first row. A
#     ls-remote that lists other refs first would otherwise bind the wrong SHA.
cat > "$T/multi" <<'EOF'
ref: refs/heads/main	HEAD
dead0000000000000000000000000000000000ad	refs/heads/other
beef1111111111111111111111111111111111ef	HEAD
EOF
ok "15 HEAD row, not first row" "beef1111111111111111111111111111111111ef" "$(head_sha "$T/multi")"

printf '\n%d passed, %d failed\n' "$PASS" "$FAIL"
[ "$FAIL" -eq 0 ]
