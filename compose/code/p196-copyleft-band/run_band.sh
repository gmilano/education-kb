# Runs ACTION P196-B's band over every copyleft row in p195's census.
# Input: the census TSV (slug, licence_path, bytes, family, probes, worst_http, verdict)
# Output: slug  path  bytes  family  band_verdict  delta_to_nearest_edge
set -u
_HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
. "$_HERE/band_copyleft.sh"
CENSUS="${1:?census tsv}"
printf 'slug\tpath\tbytes\tfamily\tband_verdict\tdelta_bytes\n'
tail -n +2 "$CENSUS" | awk -F'\t' '$4 ~ /^(AGPL-3\.0|GPL-3\.0|GPL-2\.0|LGPL-3\.0|LGPL-2\.1|MPL-2\.0|ECL-2\.0)$/ {print $1"\t"$2"\t"$3"\t"$4}' \
| while IFS=$'\t' read -r slug path sz fam; do
    bv="$(band_verdict "$fam" "$sz")"
    d=0
    if [ "$bv" = UNDER ] || [ "$bv" = OVER ]; then
      best=
      for iv in $(band_set_of_family "$fam"); do
        lo="${iv%%:*}"; hi="${iv##*:}"
        if [ "$sz" -lt "$lo" ]; then c=$((lo-sz)); else c=$((sz-hi)); fi
        [ -z "$best" ] || [ "$c" -lt "$best" ] && best="$c"
      done
      d="$best"
    fi
    printf '%s\t%s\t%s\t%s\t%s\t%s\n' "$slug" "$path" "$sz" "$fam" "$bv" "$d"
  done
