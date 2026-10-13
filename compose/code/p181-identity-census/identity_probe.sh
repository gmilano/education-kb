#!/usr/bin/env bash
# p181 ACTION LK — identity-class probe over ai-tutor / intelligent-tutoring-system rows.
#
# Method notes (both are corrections this KB owes itself):
#   * git grep -I  excludes BINARY files. p181 found `git grep -ilw lti` in Selleo/mentingo
#     matching a .webp, a .png and an .mp4 — byte coincidences reported as capability.
#   * word-bounded -w only; counts are FILE counts over TRACKED files in a --depth 1 clone.
#   * a count is a pointer to a read, never a substitute for one (T288). This script emits
#     the evidence lines for the identity probes so the classification can be read, not trusted.
#
# usage: identity_probe.sh <clone-root> <slug> <stars>
set -u
ROOT="$1"; SLUG="$2"; STARS="$3"
cd "$ROOT" 2>/dev/null || { echo "${SLUG}\tCLONE_MISSING"; exit 0; }

g() { git grep -Ilw "$1" -- . 2>/dev/null | wc -l | tr -d ' '; }
gi() { git grep -Iilw "$1" -- . 2>/dev/null | wc -l | tr -d ' '; }

FILES=$(git ls-files 2>/dev/null | wc -l | tr -d ' ')
HEAD=$(git rev-parse --short=12 HEAD 2>/dev/null)

# licence payload
LIC_F=""; for f in LICENSE LICENSE.md LICENCE LICENSE.txt COPYING COPYING.txt LICENSE-MIT; do
  [ -f "$f" ] && { LIC_F="$f"; break; }
done
if [ -n "$LIC_F" ]; then
  LIC_B=$(stat -c%s "$LIC_F"); LIC_MD5=$(md5sum "$LIC_F" | cut -d' ' -f1)
  LIC_KIND=$(head -3 "$LIC_F" | tr '\n' ' ' | cut -c1-60)
else
  LIC_B=0; LIC_MD5="-"; LIC_KIND="NO-LICENCE-FILE"
fi

# identity probes
AUTH=$(gi auth); LOGIN=$(gi login); JWT=$(gi jwt); OAUTH=$(gi oauth)
BCRYPT=$(gi bcrypt); PASSWD=$(gi password); SESSION=$(gi session); TENANT=$(gi tenant)
PASSKEY=$(gi passkey); SAML=$(gi saml); LDAP=$(gi ldap)

# persistence probes (entity declarations, not prose)
TBL_PY=$(git grep -Ic "__tablename__" -- '*.py' 2>/dev/null | awk -F: '{s+=$NF} END {print s+0}')
TBL_DRIZZLE=$(git grep -Ic "pgTable(\|sqliteTable(\|mysqlTable(" -- '*.ts' '*.js' 2>/dev/null | awk -F: '{s+=$NF} END {print s+0}')
TBL_PRISMA=$(git grep -Ic "^model " -- '*.prisma' 2>/dev/null | awk -F: '{s+=$NF} END {print s+0}')
TBL_SQL=$(git grep -Iic "CREATE TABLE" -- '*.sql' 2>/dev/null | awk -F: '{s+=$NF} END {print s+0}')
TBL_JPA=$(git grep -Ic "@Entity" -- '*.java' '*.kt' 2>/dev/null | awk -F: '{s+=$NF} END {print s+0}')
TBL_MONGO=$(git grep -Ic "mongoose.model(\|new Schema(" -- '*.ts' '*.js' 2>/dev/null | awk -F: '{s+=$NF} END {print s+0}')
TABLES=$((TBL_PY+TBL_DRIZZLE+TBL_PRISMA+TBL_SQL+TBL_JPA+TBL_MONGO))

# a user ENTITY, not the word "user"
USERENT=$(git grep -IlE "class User\(|@Entity[^)]*User|__tablename__ *= *[\"']users?[\"']|pgTable\(\"users\"|model User |CREATE TABLE[[:space:]]+\"?users?\"?" -- . 2>/dev/null | wc -l | tr -d ' ')

# server / framework presence
SRV=$(gi "express"); FASTAPI=$(gi "fastapi"); NEST=$(gi "nestjs"); FLASK=$(gi "flask")
SPRING=$(gi "springframework")

# MCP-client-credential signature (the BORROWED signature found at p180 in anki-mcp-server)
MCPCLIENT=$(git grep -Il "CLIENT_ID\|clientId\|authClientId" -- . 2>/dev/null | wc -l | tr -d ' ')
MCP=$(gi "mcp")

printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
  "$SLUG" "$STARS" "$FILES" "$HEAD" "$LIC_F" "$LIC_B" "$LIC_MD5" \
  "$AUTH" "$LOGIN" "$JWT" "$OAUTH" "$BCRYPT" "$PASSWD" "$SESSION" "$TENANT" \
  "$TABLES" "$USERENT" "$MCPCLIENT" "$MCP" "$LIC_KIND"

# evidence block to stderr so the classification can be READ
{
  echo "### $SLUG ($STARS*) HEAD=$HEAD files=$FILES tables=$TABLES(py=$TBL_PY drizzle=$TBL_DRIZZLE prisma=$TBL_PRISMA sql=$TBL_SQL jpa=$TBL_JPA mongo=$TBL_MONGO)"
  echo "    passkey=$PASSKEY saml=$SAML ldap=$LDAP express=$SRV fastapi=$FASTAPI nest=$NEST flask=$FLASK spring=$SPRING mcp=$MCP"
  if [ "$USERENT" -gt 0 ]; then
    echo "--- USER ENTITY evidence ---"
    git grep -InE "class User\(|@Entity[^)]*User|__tablename__ *= *[\"']users?[\"']|pgTable\(\"users\"|model User |CREATE TABLE[[:space:]]+\"?users?\"?" -- . 2>/dev/null | head -6
  fi
  if [ "$JWT" -gt 0 ] || [ "$BCRYPT" -gt 0 ]; then
    echo "--- TOKEN/HASH evidence ---"
    git grep -Iin "create_access_token\|createAccessToken\|refresh_token\|refreshToken\|bcrypt\.\|hashSync\|jwt\.sign\|jose" -- . 2>/dev/null | head -6
  fi
  if [ "$MCPCLIENT" -gt 0 ] && [ "$USERENT" -eq 0 ]; then
    echo "--- BORROWED-identity candidate: client-credential sites ---"
    git grep -In "CLIENT_ID\|authClientId" -- . 2>/dev/null | head -5
  fi
  echo
} >&2
