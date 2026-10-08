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
check "LGPL is not GPL (y ahora con version: Gap 256)" LGPL-3.0 "$(family_of "$LGPL")"
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


# ---------------------------------------------------------------------------
# CONTROL NEGATIVO 9 — P453 (pase 29).  La EUPL es la licencia de la propia Comision
# Europea y el estante publico EMEA de esta KB esta escrito en ella: nueve payloads
# reales, ocho de ellos servicios educativos nacionales finlandeses.  Este clasificador
# NO la tenia y devolvia UNCLASSIFIED sobre los nueve, mientras el lado Python la
# resolvia desde el pase 26 -- la asimetria exacta que P445 nombro.
#
# LOS DOS CONTROLES NEGATIVOS SON EL PUNTO, y van en las dos direcciones:
#
#   (1) EUPL NO LE ROBA A NADIE.  El Apendice de EUPL-1.2 lista por NOMBRE a GPL-2.0,
#       AGPL-3.0, LGPL-2.1, MPL-2.0 y EPL-1.0 como licencias compatibles.  Si la rama
#       EUPL matcheara la mencion desnuda de esos nombres, un payload EUPL se clasificaria
#       bien pero por la razon equivocada; y al reves, la rama EUPL va PRIMERA, asi que si
#       matcheara de mas se quedaria con payloads GPL/MPL/EPL legitimos.  Se afirma que no.
#
#   (2) NADIE LE ROBA A LA EUPL.  Es la razon del orden: un payload EUPL trae las marcas
#       de cinco familias ajenas, asi que cualquier rama de abajo se lo lleva si corre
#       antes.  El fixture EUPL_APPENDIX trae el Apendice COMPLETO justamente para eso.
EUPL12='European Union Public Licence
V. 1.2

EUPL (C) the European Union 2007, 2016

This European Union Public Licence (the EUPL) applies to the Work (as defined
below) which is provided under the terms of this Licence.'
EUPL11='This project is licensed under the EUPL, Version 1.1 or - as soon they will be
approved by the European Commission - subsequent versions of the EUPL.'
# El Apendice real: cinco familias ajenas NOMBRADAS dentro de un payload EUPL.
EUPL_APPENDIX='European Union Public Licence
V. 1.2

Appendix

Compatible Licences according to Article 5 EUPL are:
- GNU General Public License (GPL) v. 2, v. 3
- GNU Affero General Public License (AGPL) v. 3
- Mozilla Public Licence (MPL) v. 2
- Eclipse Public License (EPL) v. 1.0
- CeCILL v. 2.0, v. 2.1
- Common Development and Distribution License (CDDL) v. 2.'
check "P453 EUPL-1.2 texto canonico"              EUPL-1.2 "$(family_of "$EUPL12")"
check "P453 EUPL-1.1 aviso corto"                 EUPL-1.1 "$(family_of "$EUPL11")"
check "P453 EUPL con Apendice: no la roba GPL"    EUPL-1.2 "$(family_of "$EUPL_APPENDIX")"
check "P453 EUPL uso comercial ALLOWED"           ALLOWED  "$(cu "$EUPL12")"
check "P453 EUPL invariante a reflujo 70"         EUPL-1.2 "$(family_of "$(printf '%s' "$EUPL12" | reflow 70)")"
# NEG: la mencion desnuda de la sigla no licencia nada.  Un MIT que REMITE a la EUPL
# sigue siendo MIT; el Apendice de OTRA licencia que nombra la EUPL no la hereda.
check "P453 NEG EUPL no roba un MIT que la menciona" MIT "$(family_of "MIT License

Copyright (c) 2026 X
Permission is hereby granted, free of charge.  Some vendored parts are EUPL.")"
check "P453 NEG EUPL no roba un Apache que la menciona" Apache-2.0 "$(family_of "                                 Apache License
                           Version 2.0, January 2004
   Interoperable with the European Union Public Licence where required.")"
check "P453 NEG mencion desnuda de la sigla no clasifica" UNCLASSIFIED "$(family_of "See the EUPL for details about reuse of European public sector software.
This file is a pointer and grants nothing by itself.")"
# NEG en la direccion de P171: GPL-2.0 real NO se vuelve EUPL por nombrarse en su Apendice.
check "P453 NEG GPL-2.0 sigue GPL-2.0"            GPL-2.0  "$(family_of "$GPL2")"
check "P453 NEG GPL-3.0 sigue GPL-3.0 (seccion 13)" GPL-3.0 "$(family_of "$GPL3")"


# ---------------------------------------------------------------------------
# CONTROL NEGATIVO 10 — P454/P455/P456 (pase 29).  Los tres defectos que el re-run de
# `p445` destapo DESPUES de que las dos ramas EUPL/NC entraran: los 29 desacuerdos que
# quedaban no eran «filas de preambulo GPLv2», eran TRES CLASES NOMBRABLES, y en dos de
# las tres el clasificador equivocado era ESTE, el endurecido.
#
# P454 — MPL-2.0 seccion 1.12 DEFINE «Secondary License» nombrando la GPL-2.0, la
# LGPL-2.1 y la AGPL-3.0, asi que todo payload MPL trae las tres marcas GNU.  El pase 26
# arreglo esto en el lado Python y el arreglo NO VIAJO: cinco repos MPL-2.0 de este
# estante volvian GPL-3.0 aca.  El fixture es el titulo real de `dequelabs/axe-core`.
MPL_SECONDARY='Mozilla Public License, version 2.0

1. Definitions

1.12. "Secondary License" means either the GNU General Public License, Version 2.0, the
GNU Lesser General Public License, Version 2.1, the GNU Affero General Public License,
Version 3.0, or any later versions of those licenses.'
check "P454 MPL-2.0 con 1.12 no la roba la familia GNU" MPL-2.0 "$(family_of "$MPL_SECONDARY")"
check "P454 MPL-2.0 permite uso comercial"              ALLOWED "$(cu "$MPL_SECONDARY")"
EPL='Eclipse Public License - v 2.0

THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS ECLIPSE PUBLIC LICENSE.'
# P560 (pase 46).  LA AFIRMACION DE P454 ES INDEPENDIENTE DE LA VERSION, y escribirla como
# `expected=EPL` la ataba a que la rama EPL fuera SIN VERSIONAR -- que es exactamente el defecto
# que P560 arreglo.  Cuando la rama empezo a LEER la version este check se puso rojo sin que la
# propiedad que afirma hubiera cambiado en nada: el payload sigue sin ser robado por GNU.  Se
# reescribe como la INVARIANTE que siempre fue («la familia es EPL, no una GNU»), asi que no
# vuelve a romperse cuando aparezca EPL-1.0 u otra version; la afirmacion de VERSION se hace
# aparte, en la linea de abajo, que es donde corresponde.
check "P454 EPL no robada por GNU (invariante: familia EPL)" EPL "$(family_of "$EPL" | cut -d- -f1)"
check "P560 el fixture de P454 dice v2.0 y ahora SE LEE"     EPL-2.0 "$(family_of "$EPL")"
# Y el control en la direccion contraria: MPL/EPL suben, asi que no pueden quedarse con
# un GPL legitimo que las mencione.  GPL-3.0 no nombra a Mozilla ni a Eclipse, pero la
# afirmacion se hace igual porque es la premisa del reordenamiento.
check "P454 NEG GPL-3.0 real sigue GPL-3.0"             GPL-3.0 "$(family_of "$GPL3")"
check "P454 NEG GPL-2.0 real sigue GPL-2.0"             GPL-2.0 "$(family_of "$GPL2")"

# P455 — la concesion EN PROSA con el titulo en caja mixta.  Fixture: el `LICENSE` real de
# `ankitects/anki`, que volvia `CC-BY-SA-4.0` -- un AGPL-3.0 reportado como licencia de
# contenido.  El control negativo que importa es la seccion 13 de GPL-3.0, que dice
# «licensed under VERSION 3 OF the GNU Affero...»: otra preposicion, y por eso no entra.
ANKI='Anki is licensed under the GNU Affero General Public License, version 3 or later,
with portions contributed by Anki users licensed under the BSD-3 license.
Documentation on this repository is licensed CC BY-SA 4.0.'
check "P455 AGPL-3.0 concedida en prosa, caja mixta"    AGPL-3.0 "$(family_of "$ANKI")"
LGPL_PROSE='This library is licensed under the GNU Lesser General Public License,
version 2.1 or later.'
# `Gap 256` (pase 53): la hermana AGPL de la linea 628 YA esperaba una respuesta CON version
# (`AGPL-3.0`); esta esperaba `LGPL` a secas tres lineas despues, sobre un payload que dice
# «version 2.1 or later». La inconsistencia vivia DENTRO de esta misma suite.
check "P455 LGPL concedida en prosa, caja mixta"        LGPL-2.1 "$(family_of "$LGPL_PROSE")"
# EL CONTROL NEGATIVO DE P455, y es el que atrapo dos intentos de este mismo pase:
# el payload de GPL-2.0 NOMBRA la LGPL en su recomendacion de cierre.  Una sonda suelta
# sobre el cuerpo se lo lleva; esta no.
GPL2_RECOMMENDS_LGPL='                    GNU GENERAL PUBLIC LICENSE
                       Version 2, June 1991

If your program is a subroutine library, you may consider it more useful to permit
linking proprietary applications with the library.  If this is what you want to do, use
the GNU Lesser General Public License instead of this License.'
check "P455 NEG GPL-2.0 que recomienda la LGPL sigue GPL-2.0" GPL-2.0 \
      "$(family_of "$GPL2_RECOMMENDS_LGPL")"

# P456 — una FRASE DE CONCESION vence a una SIGLA de clausula.  Fixture: la forma real de
# `pupilfirst/pupilfirst`, que declara CC BY-SA para `docs/` y MIT para el software.
PUPILFIRST='Copyright (c) 2013-present Example Pvt. Ltd.

Portions of this software are licensed as follows:

* All content residing under the "docs/" directory of this repository is licensed under
  "Creative Commons: CC BY-SA 4.0 license".
* Content outside of the above mentioned restrictions is available under the "MIT"
  license as defined below.

Permission is hereby granted, free of charge, to any person obtaining a copy of this
software and associated documentation files.'
check "P456 aviso mixto: el software es MIT, no la clausula de docs" MIT \
      "$(family_of "$PUPILFIRST")"
check "P456 el aviso mixto permite uso comercial"       ALLOWED "$(cu "$PUPILFIRST")"
# LOS DOS CONTROLES NEGATIVOS DE P456: las anclas que subieron no pueden robarle un
# payload CC real, porque el texto legal de CC no contiene ninguna de las dos frases.
check "P456 NEG CC BY-NC-SA real sigue CC-BY-NC-SA-4.0" CC-BY-NC-SA-4.0 "$(family_of "$CCNCSA")"
check "P456 NEG CC BY-NC-SA real sigue PROHIBIDO"       PROHIBITED      "$(cu "$CCNCSA")"


# ---------------------------------------------------------------------------
# CONTROL NEGATIVO 11 — P457 (pase 29).  El payload GNU SIN TITULO.  Tres repos de este
# estante lo traen (`kuali/kc`, `kuali/kfs`, `untisapi/untis4j`): el texto completo con el
# titulo borrado, identificandose solo en el Preambulo.  La oracion autoidentificatoria es
# el discriminador, y el ORDEN entre las tres es forzado porque el texto de LGPL-3.0
# tambien nombra a la GPL-3.0.
AGPL_NOTITLE='Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies of this license document.

Preamble
The GNU Affero General Public License is a free, copyleft license for software.
"This License" refers to version 3 of the GNU Affero General Public License.'
LGPL3_NOTITLE='Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>

This version of the GNU Lesser General Public License incorporates the terms and
conditions of version 3 of the GNU General Public License, supplemented by the
additional permissions listed below.
As used herein, "this License" refers to version 3 of the GNU Lesser General Public
License, and the "GNU GPL" refers to version 3 of the GNU General Public License.'
check "P457 AGPL-3.0 sin titulo, por su oracion propia"  AGPL-3.0 "$(family_of "$AGPL_NOTITLE")"
check "P457 LGPL-3.0 sin titulo no se la lleva la GPL"   LGPL-3.0 "$(family_of "$LGPL3_NOTITLE")"
check "P457 LGPL-3.0 permite uso comercial"              ALLOWED  "$(cu "$LGPL3_NOTITLE")"
check "P457 NEG GPL-3.0 con su propia oracion sigue GPL-3.0" GPL-3.0 \
      "$(family_of 'GNU GENERAL PUBLIC LICENSE
Version 3, 29 June 2007
"This License" refers to version 3 of the GNU General Public License.')"

# ---------------------------------------------------------------------------
# P551 (pase 45 del 2026-10-07) — LA VERSION DE UN TEXTO CC SE LEE, NO SE ESTAMPA.
# La rama CC concatenaba `-4.0` literal.  Los tres payloads de abajo son REALES, bajados
# este pase de los treebanks que `Gap 246` obliga a mirar, y el primero es el que destapo
# el defecto: su bloque de titulo dice 3.0 y el clasificador contestaba 4.0.
# Para un treebank --que es una BASE DE DATOS-- 3.0 vs 4.0 es la diferencia entre no tener
# y tener los derechos sui generis del art. 4, asi que el defecto INVENTABA concesion.
# ---------------------------------------------------------------------------
# La suite hace `cd "$(dirname "$0")"` en su linea 14, asi que los fixtures son relativos
# a ese directorio.  (`${BASH_SOURCE[0]}` llega vacio en este punto y un `dirname ""` deja
# la ruta en `/fixtures-p551`: el primer intento fallo asi y los cuatro casos dieron
# UNCLASSIFIED, que es exactamente el modo en que un fixture ausente se disfraza de
# veredicto -- la forma de P502 sobre el canal de entrada de la propia suite.)
FIXP551="fixtures-p551"
check "P551 PUD real: el titulo dice 3.0 y se contesta 3.0" CC-BY-SA-3.0 \
  "$(family_of "$(cat "$FIXP551/cc-by-sa-3.0-ud-portuguese-pud.LICENSE")")"
check "P551 NEG Bosque real sigue 4.0 (el arreglo no degrada a todos)" CC-BY-SA-4.0 \
  "$(family_of "$(cat "$FIXP551/cc-by-sa-4.0-ud-portuguese-bosque.LICENSE")")"
check "P551 NEG CINTIL real: atributos NC-ND intactos y version 4.0" CC-BY-NC-ND-4.0 \
  "$(family_of "$(cat "$FIXP551/cc-by-nc-nd-4.0-ud-portuguese-cintil.LICENSE")")"
check "P551 NEG CINTIL real sigue comercialmente PROHIBIDO" PROHIBITED \
  "$(cu "$(cat "$FIXP551/cc-by-nc-nd-4.0-ud-portuguese-cintil.LICENSE")")"
# La sigla (canal 3): es como lo declara un README, y es por donde entro P312.
check "P551 sigla con version 3.0 contesta 3.0" CC-BY-SA-3.0 \
  "$(family_of "## License
CC BY-SA 3.0. ShareAlike restrictions apply.")"
check "P551 sigla con version 2.5 contesta 2.5" CC-BY-2.5 \
  "$(family_of "## License
Licensed CC BY 2.5. Attribution required.")"
# «no declara version» y «declara 4.0» son respuestas DISTINTAS (la leccion de P502).
check "P551 CC sin version alguna no se adivina en 4.0" CC-BY-SA-UNVERSIONED \
  "$(family_of "This work is licensed under a Creative Commons Attribution-ShareAlike License.")"
check "P551 NEG el texto CC-BY-SA-4.0 canonico sigue 4.0" CC-BY-SA-4.0 \
  "$(family_of "Creative Commons Attribution-ShareAlike 4.0 International Public License
You are free to share and adapt.")"
# NEG: la version de una familia OSI no se la lleva la rama CC.
check "P551 NEG Apache-2.0 no entra a la rama CC por su 2.0" Apache-2.0 \
  "$(family_of "$APACHE")"

# ---------------------------------------------------------------------------
# CONTROL NEGATIVO 14 — P560/P561 (pase 46 del 2026-10-07).  P551 arreglo «la version se
# ESTAMPA en vez de LEERSE» para la rama CC y el arreglo NO VIAJO UNA LINEA: la rama MPL
# estampaba `MPL-2.0` (P561) y la rama EPL colapsaba 1.0 y 2.0 en `EPL` (P560).  Los fixtures
# son payloads REALES, no sinteticos, y viven en `p560-epl-mpl-version-read/fixtures/`.
FIXP560="$(dirname "${BASH_SOURCE[0]}")/../p560-epl-mpl-version-read/fixtures"
if [ -d "$FIXP560" ]; then
  # P561: el texto canonico de MPL-1.1 (SPDX) contestaba MPL-2.0.
  check "P561 MPL-1.1 canonico contesta 1.1 y no el estampado 2.0" MPL-1.1 \
    "$(family_of "$(cat "$FIXP560/mpl-1.1-spdx-canonical.LICENSE")")"
  check "P561 NEG MPL-2.0 real sigue 2.0" MPL-2.0 \
    "$(family_of "$(cat "$FIXP560/mpl-2.0-rhino-partial-grant.LICENSE")")"
  # P560: cuatro payloads EPL reales, dos versiones, antes TODOS `EPL`.
  check "P560 EPL-1.0 real (junit4) se distingue de 2.0" EPL-1.0 \
    "$(family_of "$(cat "$FIXP560/epl-1.0-junit4.LICENSE")")"
  check "P560 EPL-2.0 real (Huly) se distingue de 1.0" EPL-2.0 \
    "$(family_of "$(cat "$FIXP560/epl-2.0-huly.LICENSE")")"
  # EL CONTROL QUE FIJA EL ORDEN DE LAS SONDAS.  El payload de paho nombra «Eclipse Public
  # License v2.0» Y «Eclipse Distribution License v1.0».  Si la sonda de 1.0 fuera suelta, o
  # corriera primero, este payload contestaria EPL-1.0 -- el veredicto equivocado y justo
  # sobre el eje de compatibilidad GPL.  Es el caso obligatorio de esta rama.
  check "P560 paho: EDL v1.0 en el mismo payload no degrada el EPL-2.0" EPL-2.0 \
    "$(family_of "$(cat "$FIXP560/epl-2.0-paho-with-edl-1.0.LICENSE")")"
  # Las dos familias siguen permitiendo uso comercial: ambas son OSI en toda version.
  check "P560 EPL-1.0 permite uso comercial" ALLOWED \
    "$(cu "$(cat "$FIXP560/epl-1.0-junit4.LICENSE")")"
  check "P561 MPL-1.1 permite uso comercial" ALLOWED \
    "$(cu "$(cat "$FIXP560/mpl-1.1-spdx-canonical.LICENSE")")"
  # «no declara version» y «declara una» son respuestas DISTINTAS (la leccion de P502), y la
  # rama EPL/MPL la hereda igual que la rama CC.
  check "P560 EPL sin version no se adivina" EPL-UNVERSIONED \
    "$(family_of "Eclipse Public License

THE ACCOMPANYING PROGRAM IS PROVIDED UNDER THE TERMS OF THIS AGREEMENT.")"
  check "P561 MPL sin version no se adivina en 2.0" MPL-UNVERSIONED \
    "$(family_of "Mozilla Public License

1. Definitions.")"
  # Gap 249: el licenciamiento DUAL no esta resuelto, y la suite lo AFIRMA en vez de callarlo.
  # H2 ofrece MPL-2.0 O EPL-1.0; la respuesta es un string, asi que el brazo EPL se pierde.
  check "Gap 249 dual MPL-2.0/EPL-1.0 (H2) contesta solo el brazo MPL" MPL-2.0 \
    "$(family_of "$(cat "$FIXP560/dual-mpl-2.0-or-epl-1.0-h2database.LICENSE")")"
else
  echo "SKIP P560/P561 — fixtures ausentes en $FIXP560" >&2
fi

# ---------------------------------------------------------------------------
# P613 (pase 50 del 2026-10-08) -- la rama GNU leia la FAMILIA e INVENTABA la VERSION.
#
# Es P561 verbatim en la rama que el pase 46 no audito. El `grep -qi 'Version 3'` exigia la
# PALABRA «version»; un payload que la nombra como NUMERO caia al `||` y salia GPL-2.0.
#
# LA RAZON POR LA QUE ESTA SUITE NO LO VEIA, y por eso los canonicos son casos OBLIGATORIOS
# aca: los cuatro textos canonicos de SPDX clasifican BIEN, porque todos deletrean «Version 3».
# El defecto vive SOLO en los stubs de titulo -- lo que publican los treebanks y los datasets.
FIXP613=fixtures-p613
if [ -d "$FIXP613" ]; then
  # --- el payload REAL que lo encontro: 68 B, UD_Spanish-AnCora en su tag r2.8 ---
  check "P613 stub numerico REAL (AnCora r2.8, 68 B) contesta 3.0 y no el estampado 2.0" GPL-3.0 \
    "$(family_of "$(cat "$FIXP613/gpl-3.0-numeric-ud-spanish-ancora-r2.8.LICENSE")")"
  # --- las formas de stub medidas en el pase: 4 de 5 fallaban ---
  check "P613 stub 'LICENSE 3.0' (numerico, sin la palabra version)" GPL-3.0 \
    "$(family_of 'GNU GENERAL PUBLIC LICENSE 3.0')"
  check "P613 stub 'License v3.0' (caja mixta + v)" GPL-3.0 \
    "$(family_of 'GNU General Public License v3.0')"
  check "P613 stub 'GPLv3' junto al titulo" GPL-3.0 \
    "$(family_of 'GNU GENERAL PUBLIC LICENSE
GPLv3')"
  check "P613 stub ', Version 3' (la UNICA forma que ya pasaba -- control positivo)" GPL-3.0 \
    "$(family_of 'GNU GENERAL PUBLIC LICENSE, Version 3')"
  # --- NEGATIVOS: ensanchar el discriminador de la 3 no puede robar un GPL-2.0 legitimo ---
  # El canonico de GPL-2.0 (17.337 B) tiene CERO ocurrencias de `version 3`, `v3`, `gplv3`,
  # `3.0` y `License 3`. Medido en el pase 50, no supuesto.
  check "P613 NEG canonico GPL-2.0 (SPDX, 17.337 B) sigue 2.0" GPL-2.0 \
    "$(family_of "$(cat "$FIXP613/gpl-2.0-spdx-canonical.LICENSE")")"
  check "P613 NEG canonico GPL-3.0 (SPDX, 34.674 B) sigue 3.0" GPL-3.0 \
    "$(family_of "$(cat "$FIXP613/gpl-3.0-spdx-canonical.LICENSE")")"
  check "P613 NEG stub 'LICENSE 2.0' numerico contesta 2.0, no 3.0" GPL-2.0 \
    "$(family_of 'GNU GENERAL PUBLIC LICENSE 2.0')"
  # --- el control que importa: P171 no se reabre por este ensanche ---
  check "P613 NEG seccion 13 de GPL-3.0 sigue GPL-3.0 (P171 no reabierto)" GPL-3.0 \
    "$(family_of "$GPL3")"
  check "P613 NEG AGPL-3.0 no se come la rama GPL" AGPL-3.0 "$(family_of "$AGPL3")"
  # `Gap 256`, declarado en el pase 50 y AFIRMADO aca en vez de callado (patron de Gap 249).
  # La rama LGPL lee su version SOLO del ancla de texto completo («refers to version 3 of the
  # GNU Lesser General Public License», linea 276), no del bloque de TITULO. Asi que un stub
  # LGPL contesta `LGPL` a secas AUNQUE nombre la version: medido este pase, las tres formas
  # (`Version 3, 29 June 2007`, `3.0` numerico, y sin version) dan `LGPL`, mientras el canonico
  # de SPDX (42.098 B) si da `LGPL-3.0`.
  #
  # NO es el defecto de P613: la rama GPL ESTAMPABA una version que el payload no nombra
  # (invencion); esta DESCARTA una que si nombra (sub-lectura). Una version de menos es
  # honesta y gruesa; una version equivocada hace razonar sobre las obligaciones de otra
  # licencia. Por eso P613 se arregla y Gap 256 se declara: el arreglo de LGPL mueve un
  # SEGUNDO contrato (`LGPL-2.1` no esta en `OSI_RECONOCIDAS` de p411) y P562 dice que no se
  # toca un instrumento cuyo contrato no se leyo.
  check "Gap 256 CERRADO stub LGPL que NOMBRA Version 3 ahora contesta LGPL-3.0" LGPL-3.0 \
    "$(family_of "$LGPL")"
  check "Gap 256 CERRADO stub LGPL numerico (3.0) lee la version" LGPL-3.0 \
    "$(family_of 'GNU LESSER GENERAL PUBLIC LICENSE 3.0')"
  check "Gap 256 CERRADO stub LGPL que NOMBRA Version 2.1 contesta LGPL-2.1" LGPL-2.1 \
    "$(family_of 'GNU LESSER GENERAL PUBLIC LICENSE
Version 2.1, February 1999')"
  # El payload REAL que motivo el cierre: `openeducat/openeducat_erp`, la unica plataforma
  # LGPL del estante de `verticals/solutions.md`. `p419` lo leia LGPL-3.0 desde el pase 123;
  # el clasificador COMPARTIDO contestaba `LGPL`. Ahora coinciden.
  check "Gap 256 CERRADO openeducat (payload real del estante) es LGPL-3.0" LGPL-3.0 \
    "$(family_of 'OpenEduCat is published under the GNU LESSER GENERAL PUBLIC LICENSE, Version 3 (LGPLv3), as included below. Since the LGPL is a set of additional permissions on top of the GPL, the text of t')"
  # NEG — «no nombra version» sigue siendo una respuesta PROPIA y gruesa, no una invencion.
  check "Gap 256 NEG LESSER sin version alguna sigue LGPL a secas" LGPL \
    "$(family_of 'GNU LESSER GENERAL PUBLIC LICENSE')"
  check "Gap 256 NEG el canonico LGPL-3.0 de SPDX si lee la version" LGPL-3.0 \
    "$(family_of "$(cat "$FIXP613/lgpl-3.0-spdx-canonical.LICENSE")")"
  # --- «no declara version» es una respuesta PROPIA, no un GPL-2.0 adivinado (P551/P560/P561) ---
  check "P613 GNU sin version alguna no se adivina en 2.0" GPL-UNVERSIONED \
    "$(family_of 'GNU GENERAL PUBLIC LICENSE

 Everyone is permitted to copy and distribute verbatim copies of this
 license document, but changing it is not allowed.')"
  # --- el eje de uso comercial no se mueve: GPL es OSI en toda version ---
  check "P613 el stub numerico GPL-3.0 permite uso comercial" ALLOWED \
    "$(cu "$(cat "$FIXP613/gpl-3.0-numeric-ud-spanish-ancora-r2.8.LICENSE")")"
  # --- y los vecinos del mismo directorio de fixtures, que son la razon del hallazgo ---
  check "P613 AnCora r2.9 (la MISMA ruta, relicenciada) contesta CC-BY-4.0" CC-BY-4.0 \
    "$(family_of "$(cat "$FIXP613/cc-by-4.0-ud-spanish-ancora-r2.9.LICENSE")")"
  check "P613 UD_Spanish-GSD contesta CC-BY-SA-4.0" CC-BY-SA-4.0 \
    "$(family_of "$(cat "$FIXP613/cc-by-sa-4.0-ud-spanish-gsd.LICENSE")")"
else
  echo "SKIP P613 — fixtures ausentes en $FIXP613" >&2
fi

printf '\n%d/%d\n' "$((n-fail))" "$n"
[ "$fail" = 0 ] || exit 1
