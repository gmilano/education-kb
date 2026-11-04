import sys
# p644: prepend a pass section immediately after the YAML frontmatter, preserving all history.
target, section = sys.argv[1], sys.argv[2]
body = open(target, encoding="utf-8").read()
lines = body.split("\n")
assert lines[0] == "---", f"{target}: no frontmatter"
end = next(i for i, l in enumerate(lines[1:], 1) if l == "---")
new = open(section, encoding="utf-8").read().rstrip("\n")
out = "\n".join(lines[:end+1]) + "\n\n" + new + "\n\n" + "\n".join(lines[end+1:]).lstrip("\n")
open(target, "w", encoding="utf-8").write(out)
print(f"  {target}: +{len(new.splitlines())} lines prepended, history preserved")
