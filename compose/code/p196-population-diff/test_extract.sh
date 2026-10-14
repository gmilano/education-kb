set -u
. /dev/stdin <<'FNS'
is_reserved_owner() {
  case "$1" in
    topics|orgs|users|sponsors|collections|features|about|pricing|settings|login|join) return 0 ;;
    marketplace|apps|enterprise|security|site|contact|notifications|explore|trending)  return 0 ;;
    search|new|organizations|account|codespaces|readme|stars|watching|dashboard)        return 0 ;;
  esac
  return 1
}
is_reserved_repo() {
  # p192 subtracted "repos" by hand.  v1 of THIS instrument reproduced that and then emitted
  # "repos/.." from a relative link; v2 enumerated "." and ".." and the corpus answered with
  # "repos/..." -- THREE dots.  Enumerating dot-segments is the same mistake as enumerating
  # filenames (P441): the rule is "a name with no non-dot character is not a repository".
  case "$1" in repos|repositories) return 0 ;; esac
  case "$1" in *[!.]*) return 1 ;; *) return 0 ;; esac
}
FNS
t=0;p=0
y(){ t=$((t+1)); if "$1" "$2"; then p=$((p+1)); else echo "FAIL want-true $1 $2"; fi; }
n(){ t=$((t+1)); if "$1" "$2"; then echo "FAIL want-false $1 $2"; else p=$((p+1)); fi; }
# the exclusions p192's rule names explicitly
y is_reserved_owner topics; y is_reserved_owner orgs; y is_reserved_owner users
# the one artefact p192 subtracted BY HAND -- now subtracted by rule
y is_reserved_repo repos
y is_reserved_repo ..
y is_reserved_repo ...
y is_reserved_repo ....
y is_reserved_repo .
# real owners on this shelf must survive
n is_reserved_owner moodle;  n is_reserved_owner openedx; n is_reserved_owner instructure
n is_reserved_owner sakaiproject; n is_reserved_owner overhangio; n is_reserved_owner frappe
n is_reserved_owner OS4ED;   n is_reserved_owner canyongbs; n is_reserved_owner HKUDS
n is_reserved_repo moodle;   n is_reserved_repo canvas-lms; n is_reserved_repo tutor
echo "$p/$t"; [ "$p" = "$t" ] || exit 1
