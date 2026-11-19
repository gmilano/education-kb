#!/usr/bin/env bash
# p917 — AFFILIATION FROM THE PACKAGING-METADATA LAYER.  Partial remedy for `916-G6`.
#
# `916-F8` recorded `gh api users/{owner}` as blocked and concluded every region placement must
# come from a byte-read README.  p917 found that 8 of 15 READMEs carry NO placement signal at all,
# so the README is not a sufficient channel either.
#
# 🟢 The generalisable find came from `916-G6` itself: `marceloschmitt/moodle-block_analytics_graphs`
# was placed LATAM not by its README (93 B, no signal) but by the `@copyright` line of its Moodle
# `version.php` — an INSTITUTIONAL EMAIL DOMAIN (`poa.ifrs.edu.br`).  Packaging manifests carry the
# same class of evidence in every ecosystem: author e-mail, homepage, repository URL, maintainer.
# This script reads that layer.  It reports the RAW signal and never guesses a region from an
# owner's NAME, because a name is not evidence (`913-F2`).
set -uo pipefail
OUT="${1:?usage: p917-affiliation-manifest.sh OUT.tsv slug...}"; shift
D=$(mktemp -d); trap 'rm -rf "$D"' EXIT
CAND=(setup.py setup.cfg pyproject.toml package.json composer.json version.php
      Cargo.toml build.gradle.kts pom.xml gradle.properties DESCRIPTION
      CITATION.cff CODEOWNERS .zenodo.json)
printf 'repo\tfile\tsignal_kind\tsignal\n' > "$OUT"
for slug in "$@"; do
  hit=0
  for br in main master develop; do
    for f in "${CAND[@]}"; do
      code=$(curl -sS --max-time 15 -o "$D/f" -w '%{http_code}' \
             "https://raw.githubusercontent.com/$slug/$br/$f" 2>/dev/null)
      [ "$code" = "200" ] || continue
      # e-mail domains and homepages are the two carriers of institutional identity
      # ── 917-F6.  p917's OWN FIRST CUT OF THIS SCRIPT WAS WRONG IN TWO WAYS, both recorded
      # because the failure mode is the one this base keeps re-finding: an instrument that
      # returns a confident value for a non-signal.
      #   (a) A CONSUMER MAIL HOST IS NOT AN AFFILIATION.  The first cut placed
      #       `GSU-CETLOE/lti1p3Library-python` on `gmail.com` and `christophse/django-lti-tool`
      #       on `posteo.me`.  Neither is institutional.  A PLATFORM domain (`github.io`,
      #       `central.sonatype.com`, `semver.org`) is the same error one layer out.
      #   (b) A VERSION STRING IS NOT AN E-MAIL.  npm `overrides`/`resolutions` blocks contain
      #       `pkg@1.0.1.patch`, and `[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}` matches it,
      #       so `Sphereon-Opensource/OID4VC` was "placed" on `1.0.1.patch`.
      # Domains are therefore CLASSIFIED, never just extracted, and only INSTITUTIONAL ones
      # place a row.  `.edu`, `.ac.*`, `.edu.*`, a ccTLD-bearing org domain (`lmddc.lu`) and a
      # named foundation (`digitalharbor.org`) place; everything else is reported as a non-signal.
      em=$(grep -ioE '[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}' "$D/f" \
           | sed -E 's/.*@//' | tr 'A-Z' 'a-z' | sort -u \
           | grep -vE '^[0-9.]+$' \
           | grep -vE '\.(patch|tgz|zip|json|js|ts|png|svg|md|txt|lock)$' \
           | grep -vE '^(example|test|localhost)' \
           | grep -vE '^(gmail|googlemail|outlook|hotmail|live|yahoo|proton|protonmail|pm|posteo|gmx|web|mail|icloud|me|qq|163|126|yandex|zoho|fastmail|tutanota|aol|msn)\.' \
           | grep -vE '^(users\.noreply\.github\.com|noreply\.github\.com)$' \
           | head -4 | paste -sd'; ' -)
      ur=$(grep -ioE 'https?://[A-Za-z0-9.-]+\.[A-Za-z]{2,}' "$D/f" \
           | sed -E 's#https?://##' | tr 'A-Z' 'a-z' | sort -u \
           | grep -vE '^(github\.com|raw\.githubusercontent\.com|www\.apache\.org|opensource\.org|spdx\.org|maven\.apache\.org|schema\.org|json-schema\.org|www\.w3\.org|pypi\.org|npmjs\.com|registry\.npmjs\.org|choosealicense\.com|docs\.github\.com|img\.shields\.io|codecov\.io|gnu\.org|www\.gnu\.org|creativecommons\.org)$' \
           | grep -vE '(^|\.)github\.io$|^central\.sonatype\.com$|^semver\.org$|^docs\.astral\.sh$|^keepachangelog\.com$|^editorconfig\.org$' | head -4 | paste -sd'; ' -)
      if [ -n "$em" ] || [ -n "$ur" ]; then
        printf '%s\t%s/%s\t%s\t%s\n' "$slug" "$br" "$f" \
          "$([ -n "$em" ] && printf 'EMAIL-DOMAIN' || printf 'HOMEPAGE')" \
          "$(printf '%s%s%s' "$em" "$([ -n "$em" ] && [ -n "$ur" ] && printf ' | ')" "$ur")" >> "$OUT"
        hit=1; break 2
      fi
    done
  done
  [ $hit -eq 0 ] && printf '%s\t-\tNONE\tno e-mail domain or institutional homepage in %d manifest paths\n' "$slug" "${#CAND[@]}" >> "$OUT"
done
