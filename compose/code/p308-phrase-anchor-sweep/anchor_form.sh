#!/bin/sh
# anchor_form.sh -- STATIC audit of every licence anchor in lib/license_family.sh.
#
# THE UNIT IS THE ONE THE PRE-REGISTRATION NAMED.  The pase 99 wrote its prediction about
# "ANCLAS DEL CLASIFICADOR mal escritas, no piezas", because the pase 98 had just been burned
# by a prediction whose unit ("pieza licenciada") any sweep satisfies.  So this instrument
# counts anchors, and the denominator is every licence anchor in the shared classifier -- 18.
#
# An anchor was REFLOW-FRAGILE when BOTH held:
#   (1) it was matched against the RAW payload ("$1"), not against a whitespace-normalized
#       view built with `tr -s '[:space:]' ' '`; AND
#   (2) it spanned more than one word, so a line break could land INSIDE it.
# grep is line-oriented: a multi-word phrase matched against un-normalized text cannot
# survive a newline between two of its words.  Neither condition is sufficient alone -- a
# single word cannot be split (2 fails), and a normalized input has no newlines left (1 fails).
#
# SHADOWING is the column that decides the CONSEQUENCE, and it is why P304 was not the whole
# story.  `osi_family_of` is an ordered cascade, so a fragile anchor costs nothing when an
# earlier normalized anchor already answers for the same family.  MIT had such a shadow
# ("MIT License", title block).  The Unlicense had NONE: its raw phrase was the only route to
# the family in the whole classifier, which is why it is the one that lost its family.
#
# A NINETEENTH ROW THAT IS NOT A PHRASE AT ALL.  The suite's negative control failed on a
# NORMALIZED anchor -- the AGPL section-0 definition P288 installed -- and the cause was not
# the phrase but the WINDOW: `head -40` counts LINES, so re-wrapping pushes the same text out
# of the title block.  It is listed last because it is the same defect on a different axis.
#
# Columns: form BEFORE P308 and form NOW, so the repair is auditable from the table.
# Invocation:  sh anchor_form.sh
printf 'anchor\tinput_pre\tinput_now\twords\tform_pre_P308\tform_now\tshadow\n'
e() { printf '%s\t%s\t%s\t%s\t%s\t%s\t%s\n' "$1" "$2" "$3" "$4" "$5" "$6" "$7"; }
e 'GNU AFFERO GENERAL PUBLIC LICENSE'                             '$t' '$t' 5  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'GNU LESSER GENERAL PUBLIC LICENSE'                             '$t' '$t' 5  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'refers to version 3 of the GNU Affero General Public License'  '$t' '$t' 11 TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'GNU GENERAL PUBLIC LICENSE'                                    '$t' '$t' 4  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'Educational Community License'                                 '$t' '$t' 3  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'Apache License'                                                '$t' '$t' 2  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'MIT License'                                                   '$t' '$t' 2  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'BSD Zero Clause|Zero-Clause BSD|0BSD'                          '$t' '$t' 3  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'ISC License'                                                   '$t' '$t' 2  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'Creative Commons|creativecommons.org'                          '$t' '$t' 2  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'Mozilla Public License'                                        '$t' '$t' 3  TITLE-NORMALIZED   TITLE-NORMALIZED -
e 'redistribution and use[^.]{0,40}in source and binary forms' '$nbsd' '$n' 9  TOKENS-NORMALIZED  TOKENS-NORMALIZED 'P304 repaired this one'
e 'Permission is hereby granted, free of charge'                  '$1' '$n' 7  RAW-PHRASE-FRAGILE TOKENS-NORMALIZED 'MIT License (title)'
e 'free and unencumbered software released into the public domain' '$1' '$n' 9  RAW-PHRASE-FRAGILE TOKENS-NORMALIZED NONE
e 'has not declared|is not licensed|no license has been|...'     '$dl' '$dl' 3 TOKENS-NORMALIZED  TOKENS-NORMALIZED -
e 'agpl|affero|lgpl|apache|mit|bsd  (declaration branch)'         '$d' '$d' 1  RAW-TOKEN-SAFE     TOKENS-NORMALIZED 'a word cannot be split'
e 'gpl ?v?-?3(\.0)? | gpl ?v?-?2(\.0)?  (declaration branch)'     '$d' '$d' 2  RAW-PHRASE-FRAGILE TOKENS-NORMALIZED 'needs a wrap inside "GPL 3"'
e 'non-commercial|noncommercial|not-for-profit|...'               '$d' '$d' 1  TOKENS-NORMALIZED  TOKENS-NORMALIZED -
e 'TITLE-BLOCK WINDOW (not an anchor: the bound every anchor above reads)' 'head -40' 'head -c 4000' 0 LINE-WINDOW-FRAGILE BYTE-WINDOW-INVARIANT 'cost P288 its anchor'
