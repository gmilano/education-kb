# p550 — strip heredoc bodies (shell) and triple-quoted strings (python) before scanning.
#
# Why (P550c).  The first cut of the sweep grepped raw file text and reported THREE
# definitions that do not exist: `f`, `g` and `k`, all of them fixture source quoted inside
# heredocs in the sweep's OWN suite.  A scanner that cannot tell a definition from a string
# containing one over-accuses, which is the error class of P543 -- and it surfaced here for
# the same reason P543 did: the instrument was run, not merely read.
#
# Shell: a heredoc opens with << or <<- followed by an optionally quoted delimiter, and closes
# on a line whose only content is that delimiter.  Nested openers are not possible in the same
# line position, so one state variable is enough.
# Python: triple quotes toggle; a line may open and close on itself.
BEGIN { hd=""; tq="" }
{
  line=$0
  if (lang=="sh") {
    if (hd != "") { if (line ~ "^[ \t]*"hd"[ \t]*$") hd=""; print ""; next }
    if (match(line, /<<-?[ \t]*['"'"'"]?[A-Za-z_][A-Za-z0-9_]*['"'"'"]?/)) {
      d=substr(line, RSTART, RLENGTH)
      sub(/<<-?[ \t]*/, "", d); gsub(/['"'"'"]/, "", d)
      hd=d; print line; next
    }
    print line; next
  }
  # python
  n=gsub(/"""/, "\"\"\"", line) + gsub(/'''/, "'''", line)
  cnt = 0
  tmp=$0
  while (match(tmp, /"""|'''/)) { cnt++; tmp=substr(tmp, RSTART+3) }
  if (tq != "") { if (cnt % 2 == 1) tq=""; print ""; next }
  if (cnt % 2 == 1) { tq="x"; print $0; next }
  print $0
}
