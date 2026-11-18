#!/usr/bin/env python3
"""p888 control set: family signatures must be tested for SUBSUMPTION.
BSD-2-Clause's signature is a textual SUBSET of BSD-3-Clause, so presence
matching alone reports arity=2 on every BSD-3 file. 
"""
import re
SUBSUMES={"BSD-3-Clause":{"BSD-2-Clause"}}  # BSD-3 body contains BSD-2 clauses
def families(text):
    SIG=[("Apache-2.0", r'Apache License\s*\n?\s*Version 2\.0'),
         ("MIT", r'Permission is hereby granted, free of charge, to any person obtaining a copy'),
         ("BSD-3-Clause", r'^\s*3\.\s*Neither the name'),
         ("BSD-2-Clause", r'Redistributions in binary form must reproduce the above copyright'),
         ("GPL-3.0", r'GNU GENERAL PUBLIC LICENSE\s*\n?\s*Version 3'),
         ("AGPL-3.0", r'GNU AFFERO GENERAL PUBLIC LICENSE'),
         ("MPL-2.0", r'Mozilla Public License Version 2\.0'),
         ("ISC", r'Permission to use, copy, modify, and/or distribute this software'),
         ("Unlicense", r'This is free and unencumbered software released into the public domain')]
    hits={f for f,p in SIG if re.search(p,text,re.I|re.M)}
    for parent,kids in SUBSUMES.items():
        if parent in hits: hits-=kids       # drop subsumed families
    return sorted(hits)

BSD3="""Copyright (c) 2026
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice,
2. Redistributions in binary form must reproduce the above copyright notice,
3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS"""
BSD2="""Copyright (c) 2026
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:
1. Redistributions of source code must retain the above copyright notice,
2. Redistributions in binary form must reproduce the above copyright notice,
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AS IS"""
MIT="Permission is hereby granted, free of charge, to any person obtaining a copy of this software"
AP="Apache License\nVersion 2.0, January 2004"
T=[("BSD-3 alone -> BSD-3 only (regression: p888 reported BSD-2+BSD-3)",BSD3,["BSD-3-Clause"]),
   ("BSD-2 alone -> BSD-2 only",BSD2,["BSD-2-Clause"]),
   ("MIT alone",MIT,["MIT"]),
   ("Apache alone",AP,["Apache-2.0"]),
   ("MIT+Apache concatenated -> genuine arity 2",MIT+"\n\n"+AP,["Apache-2.0","MIT"]),
   ("BSD-3 + Apache -> genuine arity 2, BSD-2 still suppressed",BSD3+"\n\n"+AP,["Apache-2.0","BSD-3-Clause"]),
   ("empty",""  ,[]),
   ("prose mentioning a licence is not a grant","This project is MIT licensed. See LICENSE.",[]),
   ("'Neither the name' not at clause 3 is not BSD-3","Neither the name appears mid-sentence here.",[]),
  ]
fail=0
for name,txt,exp in T:
    got=families(txt)
    ok = got==sorted(exp)
    if not ok: fail+=1
    print(f"{'PASS' if ok else 'FAIL'}  {name}\n        expected={sorted(exp)} got={got}")
print(f"\n{len(T)-fail}/{len(T)} controls pass")
