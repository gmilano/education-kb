#!/bin/sh
# Mide los dos controles de cada canal de `channels.tsv` y publica el veredicto
# de calibracion. Un canal que no sale CALIBRATED no puede usarse para leer una
# ausencia: ni un 404, ni ochenta y un 403 (P249).
# TSV: channel \t good_code \t bad_code \t verdict \t may_believe_negative
cd "$(dirname "$0")" || exit 1
code() { curl -s -o /dev/null -L --max-time 25 -w '%{http_code}' "$1" 2>/dev/null; }
printf 'channel\tgood_code\tbad_code\tverdict\tmay_believe_negative\n'
tail -n +2 channels.tsv | while IFS="$(printf '\t')" read -r ch good bad; do
  [ -n "$ch" ] || continue
  case "$ch" in
    github-html-head) g=$(curl -sI -o /dev/null -L --max-time 25 -w '%{http_code}' "$good" 2>/dev/null)
                      b=$(curl -sI -o /dev/null -L --max-time 25 -w '%{http_code}' "$bad"  2>/dev/null) ;;
    *)                g=$(code "$good"); b=$(code "$bad") ;;
  esac
  python3 -c "
import sys, calibrate
v = calibrate.classify_channel('$g', '$b')
print('$ch\t$g\t$b\t%s\t%s' % (v, calibrate.may_believe_negative(v)))
"
done
