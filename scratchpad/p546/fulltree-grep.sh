#!/bin/bash
# p546 — Gap 545-A, the decisive stage.
#
# Matching a quote against the README alone cannot adjudicate it: 63 of 94
# quotes "failed" that way on this shelf, and the prefix lengths gave the reason
# (DeepTutor 30/31 chars, feedbacksystem 77/78) — those quotes are the GitHub
# About line, a different field. So the payload is widened to EVERY TEXT FILE IN
# THE ARTEFACT AT HEAD, which is the strongest available test of the one thing
# p545 actually asked: is this phrase anywhere in the thing we credited?
#
# Each tree is cloned shallow, grepped, and deleted before the next, so the disk
# cost is one repository at a time rather than 65.
#
# Usage: fulltree-grep.sh <quotes.tsv: slug<TAB>id<TAB>normalised-quote> <outdir>
set -u
IN="$1"; OUT="$2"
mkdir -p "$OUT"
RES="$OUT/fulltree.tsv"
printf 'id\tslug\tverdict\tfile\n' > "$RES"
WORK="$OUT/tree"

cut -f1 "$IN" | sort -u | while IFS= read -r slug; do
  [ -z "$slug" ] && continue
  rm -rf "$WORK"
  if ! timeout 180 git clone --depth 1 --single-branch --quiet \
        "https://github.com/$slug" "$WORK" 2>/dev/null; then
    awk -F'\t' -v s="$slug" '$1==s {print $2"\t"s"\tCLONE-FAILED\t-"}' "$IN" >> "$RES"
    continue
  fi
  # Normalise the whole tree the same way the quotes are normalised: strip
  # markdown emphasis, fold typographic punctuation, collapse whitespace. Done
  # per file so a hit can name the file it was found in.
  find "$WORK" -type f -size -2M \
       -not -path '*/.git/*' \
       \( -name '*.md' -o -name '*.markdown' -o -name '*.rst' -o -name '*.txt' \
          -o -name '*.json' -o -name '*.yml' -o -name '*.yaml' -o -name '*.toml' \
          -o -name '*.html' -o -name '*.py' -o -name '*.ts' -o -name '*.tsx' \
          -o -name '*.js' -o -name '*.jsx' -o -name '*.go' -o -name '*.java' \
          -o -name 'LICENSE*' -o -name 'LICENCE*' -o -name '*.cfg' \) \
       -print0 2>/dev/null \
    | xargs -0 -r -n50 python3 -I "$(dirname "$0")/fold.py" > "$OUT/.folded" 2>/dev/null

  awk -F'\t' -v s="$slug" '$1==s {print $2"\t"$3}' "$IN" \
    | while IFS=$'\t' read -r qid q; do
        hit=$(grep -m1 -F -- "$q" "$OUT/.folded" 2>/dev/null | cut -d$'\x1f' -f1)
        if [ -n "$hit" ]; then
          printf '%s\t%s\tPASS\t%s\n' "$qid" "$slug" "${hit#$WORK/}" >> "$RES"
        else
          printf '%s\t%s\tNOT-IN-ARTEFACT\t-\n' "$qid" "$slug" >> "$RES"
        fi
      done
  rm -rf "$WORK" "$OUT/.folded"
done

echo "PASS            $(awk -F'\t' '$3=="PASS"' "$RES" | wc -l)"
echo "NOT-IN-ARTEFACT $(awk -F'\t' '$3=="NOT-IN-ARTEFACT"' "$RES" | wc -l)"
echo "CLONE-FAILED    $(awk -F'\t' '$3=="CLONE-FAILED"' "$RES" | wc -l)"
