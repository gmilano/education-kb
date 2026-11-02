#!/bin/bash
# prepend.sh <target.md> <new-section-file> : keep YAML frontmatter, insert section below it, preserve all history
t="$1"; n="$2"
head -5 "$t" > "$t.new"
cat "$n" >> "$t.new"
tail -n +6 "$t" >> "$t.new"
mv "$t.new" "$t"
echo "$t: $(wc -l < "$t") lines, frontmatter=$(sed -n '2,4p' "$t" | tr '\n' ' ')"
