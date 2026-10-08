#!/bin/sh
# P791 — the composer/packagist probe layer that `p253-registry-first-identity` never had.
#
# WHY THIS EXISTS, stated as the defect it measures:
#   Pass 61 recorded `packagist 404` and pass 62 recorded `packagist 200 — recovered`, both as
#   ORACLE-MAP lines. Neither was a host measurement: both probed a package id SHAPED LIKE THE
#   REPOSITORY SLUG (`packbackbooks/lti-1-3-php-library`). Nothing publishes that id. In the same
#   minute `monolog/monolog` answers 200 and an invented id answers 404 on that host, so the host
#   never moved. `p253`'s gate has refused to read a guess's 404 as an absence since pass 84 —
#   and `p253` was never run here, because its probe layer speaks only `registry.npmjs.org`.
#
# So this is the MISSING PROBE LAYER, not a new verdict. `verdict.py` imports `p253/identity.py`
# UNCHANGED. Per `P713`: re-measure the DATUM every pass; REUSE the instrument.
#
# Order (the registry-first order `p253` fixed, kept):
#   1. calibrate both channels (`P249`) — no discrimination, no run
#   2. ask the TREE how it spells its own package (`composer.json`, {main,master}) -> `declared`
#   3. ask packagist for the DECLARED id, and separately for the SLUG-SHAPED `guessed` id
#
# Usage: sh sweep_composer.sh < slugs.input.txt  > result.tsv
set -u
PKG=https://packagist.org/packages
RAW=https://raw.githubusercontent.com
NAP=${P791_NAP:-3}     # packagist resets the 2nd consecutive connection; space the calls
TAB=$(printf '\t')

# packagist.org RESETS the second consecutive connection from this host (measured: the
# calibration pair's 2nd leg came back `000` while the 1st leg was 200, three runs of three).
# A reset is NOT an answer, so `code` retries it with backoff instead of reporting it as one.
# This is how a per-id probe can look like a dead host: pass 61's `packagist 404` is one
# unretried reset away from this behaviour.
code () {
  _u=$1; _o=$2; _i=1
  while [ "$_i" -le 4 ]; do
    _c=$(curl -sS -o "$_o" -w '%{http_code}' --max-time 30 "$_u" 2>/dev/null)
    case "${_c:-000}" in
      000|"") sleep $((_i * NAP)); _i=$((_i + 1)) ;;
      *) printf '%s' "$_c"; return 0 ;;
    esac
  done
  printf '000'
}

# `P793`, measured this pass with a 404-discriminating control: `raw.githubusercontent.com`
# serves the DEFAULT branch for the literal ref `master` even when no `master` exists, while
# `main` 404s and an invented name 404s. So "read at master" is NOT provenance. Three of this
# sweep's manifest-bearing rows are served from `refs/heads/0.7`, `refs/heads/public` and
# `refs/heads/2.12`. The only ref oracle reachable from this host is `ls-remote --symref` (`P732`).
default_ref () {
  timeout 40 git ls-remote --symref "https://github.com/$1" HEAD 2>/dev/null \
    | awk '/^ref:/{sub(/^refs\/heads\//, "", $2); print $2; exit}'
}

head_sha () {
  timeout 40 git ls-remote "https://github.com/$1" HEAD 2>/dev/null \
    | awk 'NR==1{print substr($1,1,7); exit}'
}

calibrate () {
  g=$(code "$PKG/monolog/monolog.json" /dev/null); sleep "$NAP"
  b=$(code "$PKG/zzz-invented-p791/zzz-nope.json" /dev/null); sleep "$NAP"
  rg=$(code "$RAW/moodle/moodle/main/COPYING.txt" /dev/null)
  rb=$(code "$RAW/moodle/moodle/main/NO_SUCH_FILE_p791.txt" /dev/null)
  echo "CALIBRATE packagist good=$g bad=$b | raw good=$rg bad=$rb" >&2
  [ "$g" = "200" ] && [ "$b" = "404" ] && [ "$rg" = "200" ] && [ "$rb" = "404" ] && return 0
  echo "NO-CLAIM a channel does not discriminate: no 404 below would be evidence" >&2
  return 1
}

read_tree () {   # $1 = local json -> "name<TAB>license"
  python3 -I - "$1" <<'PYJ'
import json, sys
try:
    d = json.load(open(sys.argv[1]))
except Exception:
    print('-\t-'); raise SystemExit
n = d.get('name') or '-'
l = d.get('license')
l = ('+'.join(l) if isinstance(l, list) else l) or '-'
print(str(n) + '\t' + str(l))
PYJ
}

read_pkg () {    # $1 = local json -> "name<TAB>repo_slug<TAB>dir<TAB>maintainers<TAB>ver<TAB>time"
  python3 -I - "$1" <<'PYJ'
import json, re, sys


def slug(u):
    """`P792`: `identity.py` compares `pub_repo` to a SLUG, while every registry emits a URL
    (`git+https://github.com/o/r.git`). `p253`'s OWN probe layer emits the URL, so running
    `p253` end to end reports `PUBLISHED-BY-OTHER` for a package pointing at exactly its own
    repository — measured on `ltijs` this pass. Normalise HERE, so the gate is fed the shape
    its contract assumes. The gate is not touched."""
    u = str(u or '-')
    m = re.search(r'github\.com[:/]+([^/]+)/([^/.]+)', u)
    return '%s/%s' % (m.group(1), m.group(2)) if m else u


d = json.load(open(sys.argv[1]))['package']
vs = {k: v for k, v in d['versions'].items() if not k.startswith('dev-')}
k = max(vs, key=lambda x: vs[x].get('time') or '') if vs else None
m = ','.join(sorted(str(x.get('name', '-')) for x in d.get('maintainers', []))) or '-'
# TAB-delimited, and read back with IFS=TAB: a maintainer string containing a SPACE shifted two
# fields of krayin/laravel-crm's first run. Same class as the URL/slug defect above: a field
# whose CONTENTS do not match the shape its reader assumes.
print('\t'.join([str(d.get('name') or '-'), slug(d.get('repository')), '-', m,
                 str(k or '-'), str((vs[k].get('time') if k else '-') or '-')]))
PYJ
}

calibrate || exit 2

printf 'slug\tdefault_ref\thead_sha\tserved_at\ttree_name\tdeclared_license\ttree_name_http\tguessed_http\tpub_name\tpub_repo\tpub_dir\tpub_maintainer\tlatest\tlatest_time\tprobe_kind\n'

while IFS= read -r slug || [ -n "${slug:-}" ]; do
  [ -n "${slug:-}" ] || continue
  dref=$(default_ref "$slug"); dref=${dref:--}
  hsha=$(head_sha "$slug"); hsha=${hsha:--}
  br=-; tn=-; lic=-
  # the REAL default ref first, then the two pseudo-refs, so `served_at` records which one
  # actually produced the bytes rather than which one was guessed.
  for b in "$dref" main master; do
    [ "$b" = "-" ] && continue
    c=$(code "$RAW/$slug/$b/composer.json" /tmp/p791.cj.$$)
    if [ "$c" = "200" ]; then
      br=$b
      line=$(read_tree /tmp/p791.cj.$$)
      tn=${line%%"$TAB"*}; lic=${line#*"$TAB"}
      break
    fi
  done

  # --- the DECLARED id. Its 404 IS informative: the tree named it.
  th=-; pn=-; pr=-; pd=-; pm=-; lv=-; lt=-
  if [ "$tn" != "-" ]; then
    th=$(code "$PKG/$tn.json" /tmp/p791.pk.$$); sleep "$NAP"
    if [ "$th" = "200" ]; then
      pline=$(read_pkg /tmp/p791.pk.$$)
      oldifs=$IFS; IFS=$TAB
      # shellcheck disable=SC2086
      set -f; set -- $pline; set +f
      IFS=$oldifs
      pn=${1:--}; pr=${2:--}; pd=${3:--}; pm=${4:--}; lv=${5:--}; lt=${6:--}
    fi
  fi

  # --- the SLUG-SHAPED id: a GUESS. Probed only to SHOW it is not the host speaking.
  gh=$(code "$PKG/$slug.json" /dev/null); sleep "$NAP"

  kind=guessed
  [ "$tn" != "-" ] && kind=declared+guessed
  printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\n' \
    "$slug" "$dref" "$hsha" "$br" "$tn" "$lic" "$th" "$gh" "$pn" "$pr" "$pd" "$pm" "$lv" "$lt" "$kind"
done
rm -f /tmp/p791.cj.$$ /tmp/p791.pk.$$
