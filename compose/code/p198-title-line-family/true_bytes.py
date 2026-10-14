import sys, subprocess
# p198 FIX: read in BINARY.  Python text mode applies UNIVERSAL NEWLINES, so a CRLF file
# loses one byte per line and len(text.encode()) under-reports the file's true size.
# Caught by cross-validation: a concurrent pass read 11 560 where this instrument said 11 358.
sys.path.insert(0, sys.argv[2] if len(sys.argv) > 2 else ".")
from classify2 import family, is_grant
raw = open(sys.argv[1], "rb").read()
txt = raw.decode("utf-8", errors="replace")
crlf = raw.count(b"\r\n")
print(f"{family(txt)}\t{is_grant(txt)}\t{len(raw)}\t{len(txt.encode())}\t{crlf}")
