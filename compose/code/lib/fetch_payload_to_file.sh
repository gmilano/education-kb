# THE FETCH IDIOM — the half of the probe `lib/payload_measure.sh` deliberately does NOT own.
#
# Added at pass `179` of `2026-10-13` by `ACTION KY`, which found that `payload_measure.sh` ships
# the correct SIZING primitive (`size_of_file`) and nothing in this repository could reach it:
# `11` of the `12` stripping sites hold their payload only in a shell variable, and
# `size_of_file` takes a PATH.  The missing vocabulary was never the counter.  It was the fetch.
#
# ─── Why `curl -o` and not `var=$(curl …)` ───────────────────────────────────────────────────
#
#   | idiom                                     | trailing run | status code | boundary |
#   |-------------------------------------------|--------------|-------------|----------|
#   | `var=$(curl URL)`                         | 🔴 destroyed | 🔴 none     | n/a      |
#   | `out=$(curl -w '\n%{http_code}')` + `sed` | 🔴 destroyed | 🟢 yes      | 🔴 AMBIGUOUS |
#   | `curl -o FILE -w '%{http_code}'`          | 🟢 EXACT     | 🟢 yes      | 🟢 disjoint |
#
# The third row is the only one where the body and the status code never share a channel, so
# there is no boundary to misparse.  `p179-capture-shape/ambiguity_proof.sh` proves row 2 is
# ambiguous rather than merely lossy: payloads of `38`, `39` and `41` B all recover to the same
# `38` B with the same `md5`, so NO arithmetic correction to such a figure can be right.
#
# ⚠️ Scope, stated because the house style requires it: this file contains the NETWORK limb, so
# per `payload_measure.sh`'s own note it may be refused in environments where the offline half
# runs.  That is why it is a SEPARATE file — an instrument that cannot fetch still gets every
# offline control by sourcing `payload_measure.sh` alone.

# fetch_payload_to_file URL DEST [MAX_TIME] -> writes the body to DEST, prints the HTTP code.
# Return 0 only on a 200 with a file actually written.  The body and the code travel on DIFFERENT
# channels: the body to DEST, the code to stdout.  Nothing round-trips through a variable.
fetch_payload_to_file() {
  local url="$1" dest="$2" mt="${3:-25}" code
  code=$(curl -sS -o "$dest" --max-time "$mt" -w '%{http_code}' "$url" 2>/dev/null)
  printf '%s\n' "$code"
  [ "$code" = "200" ] && [ -f "$dest" ]
}

# fetch_raw_to_file OWNER/REPO REF PATH DEST -> the same, for raw.githubusercontent.com, which is
# the one GitHub host this environment's egress allowlist serves (`gap 110`; `github.com` and
# `api.github.com` both answer `403` through the proxy, re-measured at p179).
fetch_raw_to_file() {
  local slug="$1" ref="$2" path="$3" dest="$4"
  fetch_payload_to_file "https://raw.githubusercontent.com/$slug/$ref/$path" "$dest"
}
