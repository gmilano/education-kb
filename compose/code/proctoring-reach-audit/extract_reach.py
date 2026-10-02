#!/usr/bin/env python3
"""Build the network-reachability call graph of SEB Server's two reference
proctoring providers, and emit reach.tsv.

Why this exists (pass 46, action 2 / gap 96):
P94 of ../../compose/patterns.md published a row "methods that talk to the
remote: Jitsi 1, Zoom 2". That figure counts network primitives appearing
*literally inside* the interface method body. It is the direct-call count, not
the reachability count -- and for a budget the magnitude that matters is
"calling this SPI method causes an HTTP round trip", which is transitive.

Control (e) of the gate audits -- "no read verb that writes" -- generalises to
"no method classified as local that in fact reaches the network". This script
is that control, applied to a classification rather than to a route table.

Pure stdlib. No checkout is modified. Usage:

    python3 extract_reach.py /path/to/seb-server > reach.tsv
"""
import os
import re
import sys

# The 14 abstract methods of
# webservice/servicelayer/session/RemoteProctoringService.java, read from the
# interface at HEAD 7f45689. Kept explicit so a drift in upstream shows up as a
# coverage failure in test_reach.py rather than as a silently shorter table.
SPI_METHODS = [
    "getType",
    "testExamProctoring",
    "getProctorRoomConnection",
    "getClientRoomConnection",
    "createJoinInstructionAttributes",
    "disposeServiceRoomsForExam",
    "newCollectingRoom",
    "newBreakOutRoom",
    "disposeBreakOutRoom",
    "getDefaultReconfigInstructionAttributes",
    "mapReconfigInstructionAttributes",
    "notifyBreakOutRoomOpened",
    "notifyCollectingRoomOpened",
    "clearRestTemplateCache",
]

# A network primitive is a call that puts bytes on a socket. Two patterns,
# because one is not enough and the obvious single pattern is WRONG.
#
# 🔴 The trap, recorded because it cost this pass a re-run: a naive verb list
# containing `put` and `delete` scores `attributes.put(...)` -- an ordinary
# Map.put -- as an HTTP request. It reported 6 network calls inside Jitsi's
# createJoinInstructionAttributes and 10 inside Zoom's, two methods that never
# touch a socket. The verb alone does not identify a request; the RECEIVER does.
#
# So: unambiguous Spring verbs that collide with nothing in these files...
NET_CALL = re.compile(
    r"\.(?:exchange|getForEntity|getForObject|postForEntity|postForObject|"
    r"patchForObject|headForHeaders|optionsForAllow)\s*\("
)
# ...plus the colliding verbs ONLY when the receiver IS a template, so a real
# restTemplate.delete(url) stays in scope without readmitting Map.put.
#
# 🔴 The second trap, which defeated the first version of this pattern: the
# receiver must END at the word "restTemplate". Zoom caches its templates in a
# field called `restTemplatesCache`, which is a LinkedHashMap -- a loose
# `\w*restTemplate\w*` matched it and scored `restTemplatesCache.put(...)` and
# `.remove(...)` as HTTP requests, giving getZoomRestTemplate 2 phantom calls.
# Allowing no trailing word characters before the dot excludes it.
#
# getAccessToken is here because it is genuinely a request: OAuth2RestTemplate
# fetches the token from Zoom's token endpoint. It is how getZoomRestTemplate
# reaches the network while merely *validating* a cached template (line 1027),
# which is the least obvious round trip in this class.
NET_CALL_ON_TEMPLATE = re.compile(
    r"\b\w*[rR]estTemplate\s*\.\s*"
    r"(?:put|delete|execute|getAccessToken)\s*\("
)

# Constructing a RestTemplate is NOT a request: Jitsi builds one at line 162 and
# the actual call is the getForEntity on the next line. Counting the constructor
# would score Jitsi's helpers as networked and inflate the very figure this
# script exists to correct, so it is deliberately absent.

# Methods of the inner ZoomRestTemplate hierarchy are the provider's own HTTP
# verbs. They reach the socket through the shared `exchange` below them, so
# they are resolved by the graph, not special-cased here.

TYPE_DECL = re.compile(r"\b(?:class|interface|enum|record)\s+([A-Za-z_$]\w*)")

# Runtime guards: a @Value-injected flag consulted inside a method body, and
# the Spring profile / conditional annotations on the type (control (d)).
VALUE_FLAG = re.compile(r"@Value\(\s*\"\$\{([^}:]+)(?::([^}]*))?\}\"\s*\)\s*final\s+boolean\s+(\w+)")
TYPE_GUARD = re.compile(r"^@(WebServiceProfile|Profile|ConditionalOn\w*)", re.M)

DECL = re.compile(
    r"^[ \t]*(?:(?:public|private|protected|static|final|synchronized|abstract|"
    r"native|default)\s+)*"
    r"(?:<[^>]+>\s+)?"
    r"[A-Za-z_$][\w$<>\[\],.\s?&]*\s+"
    r"([A-Za-z_$]\w*)\s*\("
)


def strip_noise(src):
    """Blank out comments and string/char literals, preserving line structure.

    Brace counting is only sound on a text with no braces inside literals, and
    these two files carry JSON-ish payload strings. Newlines are kept so every
    reported line number still refers to the real file.
    """
    out = []
    i, n = 0, len(src)
    while i < n:
        c = src[i]
        two = src[i:i + 2]
        if two == "//":
            j = src.find("\n", i)
            j = n if j < 0 else j
            out.append(" " * (j - i))
            i = j
        elif two == "/*":
            j = src.find("*/", i + 2)
            j = n if j < 0 else j + 2
            out.append("".join(ch if ch == "\n" else " " for ch in src[i:j]))
            i = j
        elif c in "\"'":
            j = i + 1
            while j < n:
                if src[j] == "\\":
                    j += 2
                    continue
                if src[j] == c:
                    j += 1
                    break
                if src[j] == "\n":      # unterminated: do not swallow the file
                    break
                j += 1
            out.append("".join(ch if ch == "\n" else " " for ch in src[i:j]))
            i = j
        else:
            out.append(c)
            i += 1
    return "".join(out)


def methods_of(path):
    """Every method in the file with its body line range, at any nesting depth.

    Inner classes matter here: Zoom's HTTP verbs (createUser, createMeeting,
    deleteMeeting...) are members of the inner ZoomRestTemplate hierarchy, and a
    top-level-only scan cannot connect createAdHocMeeting to the socket.
    """
    raw = open(path, encoding="utf-8").read()
    clean = strip_noise(raw)
    raw_lines = raw.splitlines()
    lines = clean.splitlines()

    types = set(TYPE_DECL.findall(clean))

    found = []
    depth = 0
    pending = None          # (name, decl_line_idx) awaiting its opening brace
    stack = []              # open method bodies: (name, start_idx, depth)

    for idx, line in enumerate(lines):
        m = DECL.match(line)
        if m and not re.match(r"^[ \t]*(?:if|for|while|switch|catch|return|new|else)\b", line):
            name = m.group(1)
            # a declaration ending in ';' is abstract/interface: no body
            if ";" not in line.split("(")[0]:
                pending = (name, idx)

        for ch in line:
            if ch == "{":
                if pending:
                    stack.append((pending[0], pending[1], depth))
                    pending = None
                depth += 1
            elif ch == "}":
                depth -= 1
                if stack and stack[-1][2] == depth:
                    name, start, _ = stack.pop()
                    found.append((name, start, idx))
        if pending and ";" in line:
            pending = None      # abstract decl spanning lines

    return found, raw_lines, types


def analyse(path):
    methods, raw_lines, types = methods_of(path)
    bodies = {}
    for name, start, end in methods:
        text = "\n".join(raw_lines[start:end + 1])
        # A later definition of the same name would clobber an earlier one;
        # these two files have no such collision (asserted in test_reach.py).
        bodies.setdefault(name, []).append((start + 1, end + 1, text))

    direct = {}
    for name, occurrences in bodies.items():
        hits = 0
        for _, _, text in occurrences:
            hits += len(NET_CALL.findall(text))
            hits += len(NET_CALL_ON_TEMPLATE.findall(text))
        direct[name] = hits

    # Transitive closure over intra-file calls. Edge name -> callee when the
    # callee's identifier appears applied in the caller's body.
    callees = {}
    for name, occurrences in bodies.items():
        called = set()
        for _, _, text in occurrences:
            for other in bodies:
                if other == name:
                    continue
                if re.search(r"\b" + re.escape(other) + r"\s*\(", text):
                    called.add(other)
        callees[name] = called

    def reach(name, seen=None):
        """Shortest hop count from `name` to a network primitive, or None."""
        if seen is None:
            seen = set()
        if name in seen:
            return None
        seen = seen | {name}
        if direct.get(name, 0) > 0:
            return 0
        best = None
        for c in callees.get(name, ()):
            d = reach(c, seen)
            if d is not None and (best is None or d + 1 < best):
                best = d + 1
        return best

    rows = []
    for name in sorted(bodies):
        # control (c): a declaration whose name is a type name is a CONSTRUCTOR,
        # not a method. The first version of this extractor emitted 8 of them as
        # methods -- the same defect the gate audits of passes 44/45 found in
        # their route tables, reproduced here on a different artefact.
        kind = "ctor" if name in types else "method"
        start, end, _ = bodies[name][0]
        d = reach(name)
        rows.append({
            "kind": kind,
            "method": name,
            "line": start,
            "end": end,
            "is_spi": name in SPI_METHODS,
            "direct": direct.get(name, 0),
            "depth": d,
            "reaches": d is not None,
        })
    return rows


def guards_of(path):
    """Control (d): every guard that can turn a method into a no-op.

    Two kinds, and the second is the one a direct reading misses: the type-level
    Spring profile, and the @Value boolean flags consulted INSIDE a body.
    """
    raw = open(path, encoding="utf-8").read()
    type_guards = sorted(set(TYPE_GUARD.findall(raw)))
    flags = [(name, default or "") for _, default, name in
             ((m.group(1), m.group(2), m.group(3)) for m in VALUE_FLAG.finditer(raw))]
    used = []
    for name, default in flags:
        for m in re.finditer(r"if\s*\(\s*!?\s*this\.%s\b" % re.escape(name), raw):
            used.append((name, default, raw[:m.start()].count("\n") + 1))
    return type_guards, flags, used


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    base = os.path.join(
        root, "src/main/java/ch/ethz/seb/sebserver/webservice/servicelayer/session"
    )
    targets = [
        ("JITSI_MEET", os.path.join(base, "impl/proctoring/JitsiProctoringService.java")),
        ("ZOOM", os.path.join(base, "impl/proctoring/ZoomProctoringService.java")),
    ]
    print("# Network reachability of SEB Server proctoring providers.")
    print("# Pass 46, action 2 (gap 96). Generated by extract_reach.py -- do not hand-edit.")
    print("# depth 0 = the HTTP call is in this method's own body.")
    print("# depth N = it is N calls away; the SPI method still causes the round trip.")
    print("provider\tkind\tmethod\tline\tis_spi\tdirect_http\tdepth\treaches_network")
    for provider, path in targets:
        if not os.path.exists(path):
            sys.stderr.write("missing: %s\n" % path)
            continue
        for r in analyse(path):
            print("%s\t%s\t%s\t%d\t%s\t%d\t%s\t%s" % (
                provider, r["kind"], r["method"], r["line"],
                "yes" if r["is_spi"] else "no",
                r["direct"],
                "-" if r["depth"] is None else r["depth"],
                "yes" if r["reaches"] else "no",
            ))
    print("#")
    print("# control (d) -- guards that can make a method a no-op:")
    for provider, path in targets:
        if not os.path.exists(path):
            continue
        tg, flags, used = guards_of(path)
        print("# %s type-level: %s" % (provider, ", ".join("@" + g for g in tg) or "none"))
        for name, default in flags:
            print("# %s @Value flag: %s (default %s)" % (provider, name, default or "<none>"))
        for name, default, line in used:
            print("# %s runtime guard: this.%s consulted at line %d -> early return"
                  % (provider, name, line))


if __name__ == "__main__":
    main()
