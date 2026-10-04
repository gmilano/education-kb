#!/bin/bash
# Regression test for lib/license_family.sh.  Run: ./test_license_family.sh
#
# The fixture that matters is GPL3_S13: the real section 13 of GPL-3.0.  Any classifier that
# greps the body returns AGPL-3.0 for it.  This is the defect P171 named, p206's D2 test pinned,
# and pass 77 reintroduced in a fresh instrument -- which is why the classifier now lives in one
# file with one test instead of being retyped per sweep.
#
# NOTE ON COVERAGE, and it is the point of the test: a license classifier validated only on the
# class you care about scores 100% while broken.  Pass 77 checked five AGPL repos and got 5/5,
# because AGPL -> AGPL is right by accident.  The defect is visible ONLY on GPL-3.0 input.
# So GPL-3.0 is a REQUIRED case here, not an optional one.
set -u
cd "$(dirname "$0")" && . ./license_family.sh

GPL3='                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply.'
GPL2='                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991'
AGPL3='                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007'
LGPL='                   GNU LESSER GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007'
APACHE='                                 Apache License
                           Version 2.0, January 2004'
MIT='MIT License

Copyright (c) 2014 Transcordia

Permission is hereby granted, free of charge, to any person obtaining a copy'
MITNOTITLE='Copyright (c) 2019 fffnite

Permission is hereby granted, free of charge, to any person obtaining a copy'
BSD='Copyright (c) 2026 Someone

Redistribution and use in source and binary forms, with or without modification'
ECL='                        Educational Community License, Version 2.0'

fail=0; n=0
check() { # name expected actual
  n=$((n+1))
  if [ "$2" = "$3" ]; then printf 'ok   %-46s %s\n' "$1" "$3"
  else printf 'FAIL %-46s expected=%s got=%s\n' "$1" "$2" "$3"; fail=$((fail+1)); fi
}
check "GPL-3.0 with sec.13 is NOT AGPL (P171)" GPL-3.0   "$(family_of "$GPL3")"
check "GPL-2.0 predates the AGPL"              GPL-2.0   "$(family_of "$GPL2")"
check "real AGPL-3.0 by title"                 AGPL-3.0  "$(family_of "$AGPL3")"
check "LGPL is not GPL"                        LGPL      "$(family_of "$LGPL")"
check "Apache-2.0 by title"                    Apache-2.0 "$(family_of "$APACHE")"
check "MIT by title"                           MIT       "$(family_of "$MIT")"
check "MIT with no title line, by grant"       MIT       "$(family_of "$MITNOTITLE")"
check "BSD by grant line"                      BSD       "$(family_of "$BSD")"
check "ECL-2.0 before Apache (it names Apache)" ECL-2.0  "$(family_of "$ECL")"
check "empty payload is UNCLASSIFIED, not MIT" UNCLASSIFIED "$(family_of "")"
# the quantitative discriminator measured in pass 77
check "affero lines: GPL-3.0 payload"          3 "$(affero_lines "$GPL3")"
check "affero lines: GPL-2.0 payload"          0 "$(affero_lines "$GPL2")"

# DECLARATION FALLBACK (pass 77, frappe/education): a license FILE need not be a license TEXT.
# The size guard is the whole safety argument, so it gets a test on BOTH sides of itself.
DECL='License: GNU GPL V3'
check "one-line declaration is read"  "GPL-3.0 (declaracion)" "$(family_of "$DECL")"
check "declaration: MIT"              "MIT (declaracion)"     "$(family_of "License: MIT")"
check "declaration: AGPL before GPL"  "AGPL-3.0 (declaracion)" "$(family_of "License: AGPL-3.0")"

# -----------------------------------------------------------------------------
# P299 (pase 98).  La rama de declaracion matcheaba SUBCADENA, y "mit" es subcadena de
# permit/submit/limit/limitations/commit/omit.  Estos casos son NEGATIVOS: lo que se
# afirma es que un aviso que NIEGA la licencia no vuelve nunca como familia permisiva.
#
# Especimen real: murderszn/open-tutor ships a file NAMED `LICENSE` that declares no
# licence exists.  Antes de P299 se salvaba solo por pesar 868 B > la guarda de 400 B.
NOLIC_SHORT='Project License Status

This repository has not declared a project-wide reuse license. Nothing here is
granted. Do not submit changes or permit redistribution without written consent
from the rights holder. Limitations apply.'
check "P299: explicit refusal is NOT MIT (substring permit/submit/limit)" \
      "NO-CESSION (negativa explicita)" "$(family_of "$NOLIC_SHORT")"

# El especimen real, completo (868 B) -- por encima de la guarda de tamanio, asi que
# prueba que la negativa se mide SIN depender del largo.
NOLIC_REAL='OpenTutor — Project License Status

This repository has not declared a project-wide reuse license. This notice
documents that status and does not grant additional rights to the repository'"'"'s
original materials. Obtain the relevant rights holder'"'"'s permission when your
intended use requires it. A public GitHub repository is not itself a declaration
of an open-source or open-content license.

Third-party materials retain their own terms. In particular, the bundled
Instrument Serif font is covered by the SIL Open Font License recorded in
site/assets/instrument-serif-license.txt.'
check "P299: the real 868 B refusal is NO-CESSION, not UNCLASSIFIED" \
      "NO-CESSION (negativa explicita)" "$(family_of "$NOLIC_REAL")"

# Y la frontera de palabra, aislada: prosa con las palabras trampa y SIN negativa
# explicita no debe inventar una familia.
check "P299: 'permit'/'submit' alone never yield MIT" UNCLASSIFIED \
      "$(family_of 'Do not submit patches; permit nothing. Limitations apply here.')"
check "P299: 'apachemit' glued is not a token"        UNCLASSIFIED \
      "$(family_of 'internal notice apachemitbsd placeholder text')"
# ...y las declaraciones REALES siguen leyendose (no se gano solidez perdiendo la funcion).
check "P299: real declaration still read (punctuated)" "MIT (declaracion)" \
      "$(family_of 'License: MIT.')"
check "P299: real declaration still read (GPLv3 glued)" "GPL-3.0 (declaracion)" \
      "$(family_of 'License: GPLv3')"

# P299, los OTROS DOS EJES.  Un veredicto nuevo no vale si solo viaja al eje de familia
# (P237): la compuerta de P250 daba ALLOWED a la negativa, y holder_of le atribuia la
# razon de Apache/GPL.
if commercial_use_ok "$NOLIC_REAL"; then
  check "P299: explicit refusal does NOT permit commercial use" forbidden allowed
else
  check "P299: explicit refusal does NOT permit commercial use" forbidden forbidden
fi
check "P299: refusal has no grant to hold" \
      "NOT-APPLICABLE (NO-CESSION (negativa explicita): nothing is granted, so there is no grant to hold)" \
      "$(holder_of "$NOLIC_REAL")"
# THE GUARD: a full GPL-3.0 BODY must never reach the token match, or P171 reopens.  Padding it
# past the threshold must still yield GPL-3.0 from the TITLE, never AGPL from the sec.13 text.
check "guard holds: full GPL-3.0 body stays GPL-3.0" GPL-3.0 "$(family_of "$GPL3")"
check "guard holds: body over 400 B is not token-matched" GPL-3.0 \
      "$(family_of "$GPL3$GPL3")"
# And an unrecognisable short payload must stay UNCLASSIFIED, not guess.
check "short but unrecognisable stays UNCLASSIFIED" UNCLASSIFIED "$(family_of "see COPYRIGHT")"


# ============================================================================
# P250, pass 82 — the three families that reached the catalogue as UNCLASSIFIED,
# and the axis that matters more than any of them.
# ============================================================================

ZEROBSD='BSD Zero Clause License

Copyright (c) 2025 Someone <someone@example.com>

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted.

THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY.'
check "0BSD by title block" 0BSD "$(family_of "$ZEROBSD")"

ISCL='ISC License

Copyright (c) 2024 Someone

Permission to use, copy, modify, and/or distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.'
check "ISC is not read as 0BSD" ISC "$(family_of "$ISCL")"

CCBYSA='# Licencia Creative Commons Atribucion-CompartirIgual 4.0 Internacional (CC BY-SA 4.0)

Este repositorio se distribuye bajo los terminos de la licencia Creative Commons
Atribucion-CompartirIgual 4.0 Internacional, https://creativecommons.org/licenses/by-sa/4.0/'
check "CC BY-SA 4.0 by title block" CC-BY-SA-4.0 "$(family_of "$CCBYSA")"

CC0='Creative Commons CC0 1.0 Universal Public Domain Dedication

The person who associated a work with this deed has dedicated the work to the
public domain by waiving all of his or her rights to the work worldwide.'
check "CC0 is not read as CC-BY" CC0-1.0 "$(family_of "$CC0")"

# ---- THE case.  Real payload shape of dssg/student-early-warning, which sat in
# ---- agents/top.md reading UNCLASSIFIED while forbidding commercial use outright.
UCHI='BY DOWNLOADING THE STUDENT EARLY WARNING PROGRAM YOU AGREE TO THE FOLLOWING TERMS OF USE:

Copyright 2018.  The University of Chicago ("Chicago"). All Rights Reserved.

Permission to use, copy, modify, and distribute this software, including all object code
and source code, and any accompanying documentation (together the "Program") for academic
research or other not-for-profit scholarly purposes which are undertaken at a non-profit or
government institution and publishing in connection therewith, without fee and without a
signed licensing agreement, is hereby granted, provided that the above copyright notice,
this paragraph and the following two paragraphs appear in all copies, modifications, and
distributions. For the avoidance of doubt, educational and not-for-profit research purposes
excludes any service or part of selling a service that uses the Program. To obtain a
commercial license for the Program, contact the Technology Commercialization and Licensing,
Polsky Center for Entrepreneurship and Innovation, University of Chicago.'
check "non-commercial payload is NAMED, never UNCLASSIFIED" NONCOMMERCIAL-NOT-OSI \
      "$(family_of "$UCHI")"
# It opens with "Permission to use, copy, modify, and distribute this software" -- one word
# from ISC/0BSD.  A permissive body match would have labelled it ISC.  That is why the
# permissive families are decided on the TITLE and this one on the RESTRICTION.
if commercial_use_ok "$UCHI"; then
  check "commercial use on the UChicago payload" "forbidden" "allowed"
else
  check "commercial use on the UChicago payload" "forbidden" "forbidden"
fi

# ---- NEGATIVE CONTROLS.  The detector must not fire on anything permissive, or every
# ---- recommendable row in this KB turns into a false alarm.  This is the half of the
# ---- test that would have caught the detector being too greedy.
for pair in "GPL3:$GPL3" ; do :; done
check_ok() {  # name, payload -> commercial use must be ALLOWED
  if commercial_use_ok "$2"; then check "commercial OK: $1" allowed allowed
  else check "commercial OK: $1" allowed forbidden; fi
}
check_ok "Apache-2.0"   "$APACHE"
check_ok "MIT"          "$MIT"
check_ok "GPL-3.0"      "$GPL3"
check_ok "AGPL-3.0"     "$AGPL3"
check_ok "0BSD"         "$ZEROBSD"
check_ok "ISC"          "$ISCL"
check_ok "CC0-1.0"      "$CC0"
check_ok "CC BY-SA 4.0" "$CCBYSA"
# And the families themselves must be untouched by the new branches.
check "Apache still Apache after P250" Apache-2.0 "$(family_of "$APACHE")"
check "AGPL still AGPL after P250"     AGPL-3.0   "$(family_of "$AGPL3")"
check "empty still UNCLASSIFIED"       UNCLASSIFIED "$(family_of "")"


# ============================================================================
# The controls that the first cut of P250 did NOT have, and that it needed.
#
# The detector shipped a body token match and reported three AGPL-3.0 repos and
# The Unlicense as commercial-use PROHIBITED. The negative controls above did not
# catch it because they used TRUNCATED fixtures -- title blocks with no section 6
# and no grant sentence. A fixture short enough to be convenient is short enough
# to miss the defect. These two carry the exact sentences that caused the error.
# ============================================================================

# Section 6 of the real GPL-3.0/AGPL-3.0 text. "noncommercially" here describes a
# CONDITION on conveying object code, not a restriction on the licensee.
AGPL_S6='                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

  Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

                       TERMS AND CONDITIONS

  6. Conveying Non-Source Forms.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.  A separable portion of the object code,
    whose source code is excluded from the Corresponding Source as a
    System Library, need not be included in conveying the object code
    work.  Such an alternative is allowed only occasionally and
    noncommercially, and only if you received the object code with such
    an offer, in accord with subsection 6b.'
check "AGPL-3.0 body with section 6 is still AGPL-3.0" AGPL-3.0 "$(family_of "$AGPL_S6")"
if commercial_use_ok "$AGPL_S6"; then
  check "AGPL sec.6 'noncommercially' is NOT a commercial-use ban" allowed allowed
else
  check "AGPL sec.6 'noncommercially' is NOT a commercial-use ban" allowed forbidden
fi

# The Unlicense. It GRANTS permission using the very token the detector matched on.
UNLIC='This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain.'
check "The Unlicense is a NAMED family, not UNCLASSIFIED" Unlicense "$(family_of "$UNLIC")"
if commercial_use_ok "$UNLIC"; then
  check "The Unlicense permits commercial use (it says so)" allowed allowed
else
  check "The Unlicense permits commercial use (it says so)" allowed forbidden
fi

# THE GATE itself: an identified OSI family is never token-matched, so no OSI payload
# can ever come back PROHIBIDO however its body is worded.
check "gate: osi_family_of is what decides whether tokens run" AGPL-3.0 \
      "$(osi_family_of "$AGPL_S6")"
# ...and the restriction detector still fires when there is NO family to gate on.
if commercial_use_ok "$UCHI"; then
  check "gate does not disarm the real restriction" forbidden allowed
else
  check "gate does not disarm the real restriction" forbidden forbidden
fi

# CONTROL NEGATIVO: la compuerta de P250 sigue intacta para una familia OSI real.
if commercial_use_ok "$AGPL_S6"; then
  check "P299 does not disarm the P250 gate (AGPL still allowed)" allowed allowed
else
  check "P299 does not disarm the P250 gate (AGPL still allowed)" allowed forbidden
fi


# ---------------------------------------------------------------------------
# P304 (pase 99) — FRASE CONTIGUA vs TOKENS ORDENADOS, el tercer eje del mismo defecto.
#
# El especimen es REAL, no sintetico: `instructure/QTIMigrationTool`, `LICENSE.txt` 1.392 B,
# BSD-3-Clause de la University of Cambridge.  Inserta DOS cosas dentro de la oracion de
# concesion -- un complemento y un parentetico -- y el ancla de frase contigua no matchea.
#
# POR QUE ESTE CASO ES OBLIGATORIO Y NO OPCIONAL (P126 pt.2).  La fixture BSD que esta suite
# ya tenia es la oracion CANONICA, o sea el unico caso donde el ancla de frase no puede
# fallar: 50/50 pasaba con el defecto puesto.  Una fixture canonica valida la rama feliz y
# certifica un classificador roto -- es el mismo error que el pase 55 cometio midiendo
# `PASS` contra `PASS`, y el que P288 encontro midiendo AGPL en MAYUSCULAS contra AGPL en
# MAYUSCULAS.  La variante con insercion es el caso que ejercita el fallo.
BSD_INSERTED='Copyright (c) 2004-2008, University of Cambridge.
GUI Code Copyright (c) 2004-2008, Pierre Gorissen

All rights reserved.

Redistribution and use of this software in source and binary forms
(where applicable), with or without modification, are permitted
provided that the following conditions are met:'
check "P304: BSD con insercion en la oracion de concesion" BSD "$(family_of "$BSD_INSERTED")"

# La fixture canonica NO se toca: el arreglo es una relajacion del hueco, no un contrato nuevo.
check "P304: la BSD canonica sigue clasificando" BSD "$(family_of "$BSD")"

# CONSECUENCIA DE METODO, y es la razon por la que este defecto se arregla aunque pierda
# en la direccion segura.  Con la familia en UNCLASSIFIED la compuerta de P250 NO corta, y
# el veredicto de uso comercial de un payload PERMISIVO lo producia el token-match sobre el
# CUERPO, que es la via que P171 declara insegura: ALLOWED correcto por la via equivocada.
# Lo que se afirma aca es la COMPUERTA, no la respuesta -- la respuesta ya era ALLOWED.
check "P304: la familia identificada es lo que ARMA la compuerta de P250" BSD \
      "$(osi_family_of "$BSD_INSERTED")"
if commercial_use_ok "$BSD_INSERTED"; then
  check "P304: BSD-3-Clause permite uso comercial, POR LA COMPUERTA" allowed allowed
else
  check "P304: BSD-3-Clause permite uso comercial, POR LA COMPUERTA" allowed forbidden
fi

# BSD carga el titular en el texto de concesion por construccion, asi que una vez que la
# familia se reconoce, `holder_of` entra por la rama que PREGUNTA en vez de la de
# UNCLASSIFIED -- y devuelve el titular del artefacto, no prosa del cuerpo.
case "$(holder_of "$BSD_INSERTED")" in
  *"University of Cambridge"*) check "P304: holder_of entra por la rama BSD" ok ok ;;
  *)                           check "P304: holder_of entra por la rama BSD" ok \
                                     "$(holder_of "$BSD_INSERTED")" ;;
esac

# CONTROL NEGATIVO 1 — el hueco NO cruza una oracion.  Sin el `[^.]` esta relajacion
# convertiria en BSD a cualquier texto que nombre las dos mitades en oraciones distintas,
# que es precisamente como las nombra una NEGATIVA de redistribucion.
NOT_BSD_TWO_SENTENCES='Copyright (c) 2026 Alguien

This notice governs redistribution and use. In source and binary forms
this software may not be redistributed without written consent.'
case "$(family_of "$NOT_BSD_TWO_SENTENCES")" in
  BSD) check "P304 control negativo: dos oraciones distintas NO son BSD" not-BSD BSD ;;
  *)   check "P304 control negativo: dos oraciones distintas NO son BSD" not-BSD not-BSD ;;
esac

# CONTROL NEGATIVO 2 — el limite de 40 es un limite y se declara como tal.  Una insercion
# mas larga que el limite NO matchea, y eso es una COTA CONOCIDA del instrumento, no un
# descuido: se afirma para que el proximo pase la encuentre medida en vez de suponerla.
NOT_BSD_LONG_GAP='Copyright (c) 2026 Alguien

Redistribution and use of the whole of this particular software distribution
and every one of its parts in source and binary forms are permitted.'
case "$(family_of "$NOT_BSD_LONG_GAP")" in
  BSD) check "P304 cota declarada: insercion > 40 chars NO matchea" not-BSD BSD ;;
  *)   check "P304 cota declarada: insercion > 40 chars NO matchea" not-BSD not-BSD ;;
esac

# CONTROL NEGATIVO 3 — la relajacion no toca a NINGUNA otra familia.  El riesgo de aflojar
# un ancla es que se coma payloads de otras familias, y las dos que comparten vocabulario
# de redistribucion con BSD son las que hay que afirmar.
check "P304 no se come a la GPL-3.0 (seccion 13 intacta)" GPL-3.0 "$(family_of "$GPL3")"
check "P304 no se come a la Apache-2.0"                   Apache-2.0 "$(family_of "$APACHE")"
check "P304 no se come al MIT"                            MIT        "$(family_of "$MIT")"
check "P304 no se come a la ISC"                          ISC        "$(family_of "$ISCL")"
check "P304 no se come a la 0BSD"                         0BSD       "$(family_of "$ZEROBSD")"

# ---------------------------------------------------------------------------
# P308 (pase 100) — el REFLUJO como eje, y los dos controles que lo cierran.
#
# Un payload se re-envuelve sin cambiar una palabra (`fill-paragraph` de Emacs usa
# fill-column 70, `fmt` 75) y esta base ya tiene el especimen REAL de la direccion inversa
# en `p288/fixtures/agpl-3.0-kuali-kfs-reflowed.LICENSE`.  Las aserciones de abajo afirman
# que el veredicto NO depende de donde caen los saltos de linea — ni la familia, ni el
# veredicto comercial, que es el que llega a un entregable.
#
# Los dos casos que fallaban antes del arreglo, medidos sobre payloads reales:
#   - Unlicense a fill-column 70: el ancla ocupa las columnas 9..70 de una primera linea de
#     71, el corte cae DENTRO, se pierde la familia, se ABRE la compuerta de P250 y el
#     token-match sobre el cuerpo encuentra «commercial or NON-COMMERCIAL» — que es la frase
#     con la que el Unlicense CONCEDE.  Veredicto: NONCOMMERCIAL-NOT-OSI sobre el texto mas
#     permisivo que existe.  Direccion de P299 (inventa restriccion), no de P304.
#   - AGPL-3.0 a fill-column 70: el ancla de la seccion 0 que P288 instalo es NORMALIZADA y
#     se perdia igual, porque la VENTANA del bloque de titulo contaba LINEAS (`head -40`).
#     Caia por la rama GPL de abajo, que matchea el preambulo de la propia AGPL: GPL-2.0.
reflow() { fold -s -w "$1"; }

UNLIC='This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.'

# CONTROL NEGATIVO 4 — la familia es invariante al reflujo, y el Unlicense es el caso.
for w in 72 70 64 40 20; do
  check "P308 Unlicense invariante a fill-column $w" Unlicense "$(family_of "$(printf '%s' "$UNLIC" | reflow $w)")"
done

# CONTROL NEGATIVO 5 — y el veredicto COMERCIAL tambien, que es el que decide si una fila
# de esta KB puede entrar a una propuesta.  Sin esta asercion el arreglo se podria revertir
# sin que ninguna suite lo notara, porque la familia y el permiso son preguntas distintas.
for w in 70 40; do
  if commercial_use_ok "$(printf '%s' "$UNLIC" | reflow $w)"; then
    check "P308 Unlicense uso comercial ALLOWED a $w" ALLOWED ALLOWED
  else
    check "P308 Unlicense uso comercial ALLOWED a $w" ALLOWED PROHIBITED
  fi
done

# CONTROL NEGATIVO 6 — la ventana en BYTES no afloja P171.  Es la contracara obligatoria del
# arreglo: ensanchar o mover una ventana es exactamente como se reabre el par GPL/AGPL, que es
# el par que P171 existe para proteger.  La seccion 13 de la GPL-3.0 esta en el byte 28.272 del
# payload de moodle y la ventana son 4.000, asi que queda fuera por un factor de 7 — y se
# afirma con el payload envuelto, no solo con el original.
for w in 70 40; do
  check "P308 GPL-3.0 sigue GPL-3.0 envuelta a $w (sec.13 fuera de ventana)" GPL-3.0 \
        "$(family_of "$(printf '%s' "$GPL3" | reflow $w)")"
  check "P308 Apache-2.0 invariante a $w"  Apache-2.0 "$(family_of "$(printf '%s' "$APACHE" | reflow $w)")"
  check "P308 MIT invariante a $w"         MIT        "$(family_of "$(printf '%s' "$MIT" | reflow $w)")"
  check "P308 ISC invariante a $w"         ISC        "$(family_of "$(printf '%s' "$ISCL" | reflow $w)")"
  check "P308 0BSD invariante a $w"        0BSD       "$(family_of "$(printf '%s' "$ZEROBSD" | reflow $w)")"
done

# ---------------------------------------------------------------------------
# CONTROL NEGATIVO 7 — P312 (pase 101).  EL CASO QUE ESTA SUITE NO TENIA, y la razon de que
# no lo tuviera es la regla de P126 punto 2: la suite llego a 79/79 con la rama CC ROTA,
# porque ninguna de sus 79 aserciones le pasaba un payload de Creative Commons.
#
# Dos defectos distintos, y el segundo es el grave:
#   D1 — la rama CC elegia por ORDEN entre atributos ORTOGONALES: `ShareAlike` iba antes de
#        `NonCommercial`, asi que CC BY-NC-SA volvia `CC-BY-SA-4.0` y el atributo NC se perdia.
#   D2 — la compuerta de P250 («familia identificada -> comercial por definicion») tenia
#        DETRAS cuatro familias que no son OSI, asi que `CC-BY-NC-4.0` --cuyo NOMBRE dice
#        NonCommercial-- volvia uso comercial PERMITIDO.
#
# El payload de D1 no es una fixture inventada: es la licencia del corpus TalkMoves tal como
# la declara `devissaputra/classroom_discourse_intelligence/data/README.md`, medida en el
# pase 101.  El repo es MIT en el CODIGO y CC BY-NC-SA 4.0 en los DATOS.
CCNCSA='Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
NonCommercial and ShareAlike restrictions apply.  This repository does not redistribute the source corpus.'
CCNC='Creative Commons Attribution-NonCommercial 4.0 International
You may not use the material for commercial purposes.'
CCSA='Creative Commons Attribution-ShareAlike 4.0 International'
CCNCND='Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International'
CCBY='Creative Commons Attribution 4.0 International'

check "P312 D1 CC BY-NC-SA no se degrada a CC-BY-SA" CC-BY-NC-SA-4.0 "$(family_of "$CCNCSA")"
check "P312 D1 CC BY-NC-ND conserva los dos atributos" CC-BY-NC-ND-4.0 "$(family_of "$CCNCND")"
check "P312 D1 CC BY-NC sigue CC BY-NC"               CC-BY-NC-4.0    "$(family_of "$CCNC")"
# Controles POSITIVOS de la misma rama: el arreglo no puede volver NC a lo que no lo es.
check "P312 D1 CC BY-SA sigue CC-BY-SA (no gana NC)"  CC-BY-SA-4.0    "$(family_of "$CCSA")"
check "P312 D1 CC BY pelada sigue CC-BY"              CC-BY-4.0       "$(family_of "$CCBY")"

# D2: el eje del PERMISO, que es el que decide si la pieza entra en un entregable.
cu() { if commercial_use_ok "$1"; then echo ALLOWED; else echo PROHIBITED; fi; }
check "P312 D2 CC BY-NC-SA uso comercial PROHIBIDO"  PROHIBITED "$(cu "$CCNCSA")"
check "P312 D2 CC BY-NC uso comercial PROHIBIDO"     PROHIBITED "$(cu "$CCNC")"
check "P312 D2 CC BY-NC-ND uso comercial PROHIBIDO"  PROHIBITED "$(cu "$CCNCND")"
# Y los positivos: la compuerta no puede cerrarse sobre lo que si permite uso comercial.
check "P312 D2 CC BY-SA uso comercial ALLOWED"       ALLOWED    "$(cu "$CCSA")"
check "P312 D2 CC BY uso comercial ALLOWED"          ALLOWED    "$(cu "$CCBY")"
check "P312 D2 MIT uso comercial ALLOWED (positivo)" ALLOWED    "$(cu "$MIT")"
check "P312 D2 Apache-2.0 uso comercial ALLOWED"     ALLOWED    "$(cu "$APACHE")"
# P312 segundo tramo: la SIGLA como puerta de entrada a la rama CC, y los dos controles
# NEGATIVOS que la acotan -- la sigla no puede robarle un payload a una familia OSI.
CCSIGLA='## License
CC BY-NC-SA 4.0. **Non-commercial** and ShareAlike restrictions apply.'
check "P312 sigla sola: CC BY-NC-SA reconocida" CC-BY-NC-SA-4.0 "$(family_of "$CCSIGLA")"
check "P312 sigla sola: comercial PROHIBIDO"    PROHIBITED      "$(cu "$CCSIGLA")"
check "P312 NEG sigla no roba un MIT que la menciona" MIT "$(family_of "MIT License
Copyright (c) 2026 X
Permission is hereby granted, free of charge.  Docs are CC BY 4.0.")"
check "P312 NEG sigla no roba un Apache que la menciona" Apache-2.0 "$(family_of "                                 Apache License
                           Version 2.0, January 2004
   Documentation is licensed CC BY-SA 4.0.")"
check "P312 D2 AGPL-3.0 uso comercial ALLOWED"       ALLOWED    "$(cu "$AGPL3")"

# D1/D2 bajo REFLUJO, que es la invariante que P308 instalo: el arreglo de P312 no puede
# depender de donde caen los saltos de linea del payload.
for w in 70 40; do
  check "P312 CC BY-NC-SA invariante a $w" CC-BY-NC-SA-4.0 "$(family_of "$(printf '%s' "$CCNCSA" | reflow $w)")"
  check "P312 CC BY-NC-SA PROHIBIDO a $w"  PROHIBITED      "$(cu "$(printf '%s' "$CCNCSA" | reflow $w)")"
done

# ---------------------------------------------------------------------------
# CONTROL NEGATIVO 8 — P312/P237: las tres familias que vivian SOLO en la copia inline de
# `p170`.  Eran la razon DECLARADA en el pase 100 para no rewirear esa copia a esta
# libreria («adoptarla PERDERIA familias»), asi que entran aca ANTES del rewiring y la
# suite lo afirma.  Las tres son no-OSI y las tres prohiben el uso que importa.
BUSL='Business Source License 1.1

Licensor: Example Corp
Additional Use Grant: You may make production use of the Licensed Work.'
ELASTIC='Elastic License 2.0

URL: https://www.elastic.co/licensing/elastic-license'
POLYFORM='PolyForm Noncommercial License 1.0.0

<https://polyformproject.org/licenses/noncommercial/1.0.0>'
check "P312 BUSL clasificada (venia solo de p170)"     BUSL     "$(family_of "$BUSL")"
check "P312 Elastic clasificada (venia solo de p170)"  Elastic  "$(family_of "$ELASTIC")"
check "P312 PolyForm clasificada (venia solo de p170)" PolyForm "$(family_of "$POLYFORM")"
check "P312 BUSL uso comercial PROHIBIDO"     PROHIBITED "$(cu "$BUSL")"
check "P312 Elastic uso comercial PROHIBIDO"  PROHIBITED "$(cu "$ELASTIC")"
check "P312 PolyForm uso comercial PROHIBIDO" PROHIBITED "$(cu "$POLYFORM")"

printf '\n%d/%d\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
