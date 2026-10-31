#!/usr/bin/env python3
"""tool-surface.py — extract MCP tool-name declarations from a source tree.

p567. Supersedes the uncommitted line-oriented extractor used at p447 and p566,
whose four idioms were all anchored to a single physical line. The field writes
registration calls across continuation lines, so that instrument returned ZERO
tool names on 131 of 341 census rows (gap 566-B).

Idioms recognised (all multi-line tolerant, window = 6 lines after the anchor):

  A  @mcp.tool(...) / @app.tool(...) / @server.tool(...)   name= kwarg, else following def
  B  .tool( / .registerTool( / .addTool( / .setTool(       first string literal argument
  C  Tool( name=... )                                      low-level python MCP Server
  D  { name: "x", description/inputSchema ... }             JS/TS object literal in a tools array
  E  { "name": "x", ... }                                   python dict literal

Mutation verdict is taken from the tool NAME ONLY, by leading verb token, with a
small contains-list for compound names. The name axis is used because p566
retired the HTTP-verb axis for a sound reason: MCP's JSON-RPC transport is itself
POST, so every server posts and verb counting cannot separate reads from writes.

Usage: tool-surface.py TREE_ROOT [--json]
"""
import json, re, sys, os

# A multi-line @mcp.tool(description=(...), annotations=...) decorator can push the
# decorated def well past a tight window; 8 lines under-read JohannsenLum 19->5.
DEF_WINDOW = 40

# Test fixtures carry API response objects with both `name` and `description`, which
# the relaxed idiom cannot distinguish from a tool spec. They are not tool surface.
RE_TEST_PATH = re.compile(r'(^|/)(tests?|__tests__|spec|fixtures?|mocks?|examples?)(/|$)'
                          r'|(^|/)(test_|conftest)|(_test|\.test|\.spec)\.', re.I)

SRC_EXT = {'.py', '.ts', '.js', '.tsx', '.jsx', '.mts', '.cts', '.mjs', '.cjs',
           '.rs', '.go', '.java', '.rb', '.php'}
SKIP_DIR = {'node_modules', '.git', 'dist', 'build', 'vendor', '__pycache__',
            '.venv', 'venv', 'site-packages', 'target', 'coverage', '.next'}

STR = r'''["'`]([A-Za-z_][A-Za-z0-9_.\-]{1,78})["'`]'''
RE_DECOR = re.compile(r'@(?:\w+\.)?(?:tool|register_tool)\b')
RE_NAME_KW = re.compile(r'\bname\s*=\s*' + STR)
RE_DEF = re.compile(r'^\s*(?:async\s+)?def\s+(\w+)')
RE_CALL = re.compile(r'\.(?:registerTool|register_tool|addTool|add_tool|setTool|tool)\s*\(')
RE_TOOLCTOR = re.compile(r'\bTool\s*(?:\.\w+)?\s*\(')
RE_JS_NAME = re.compile(r'^\s*name\s*:\s*' + STR)
RE_PY_NAME = re.compile(r'^\s*["\']name["\']\s*:\s*' + STR)
# RELAXED: `name:` anywhere on the line, for project-local registration wrappers
# such as `get({ name: 'whoami', description: ... })`. Higher recall, lower
# precision -- never mixed with strict output, always reported as a bracket.
RE_JS_NAME_LOOSE = re.compile(r'\bname\s*:\s*' + STR)
RE_PY_NAME_LOOSE = re.compile(r'["\']name["\']\s*:\s*' + STR)
RE_FIRST_STR = re.compile(r'^\s*,?\s*' + STR)

# A declaration is a tool only if its neighbourhood looks like a tool spec, not
# an arbitrary object that happens to carry a `name` field.
RE_TOOL_LIST = re.compile(r'^\s*[A-Z][A-Z0-9_]*TOOLS?[A-Z0-9_]*\s*(?::[^=]+)?=\s*\[')
RE_LIST_REF = re.compile(r'^\s*([A-Za-z_][\w.]*)\s*,\s*$')

RE_SPEC_HINT = re.compile(r'inputSchema|input_schema|description|parameters|schema|annotations|handler|execute|callback', re.I)

MUT_VERB = {
    'create', 'add', 'update', 'delete', 'remove', 'set', 'put', 'patch', 'post',
    'submit', 'grade', 'assign', 'enroll', 'unenroll', 'upload', 'send', 'publish',
    'unpublish', 'edit', 'modify', 'write', 'mark', 'reset', 'archive', 'restore',
    'move', 'reorder', 'duplicate', 'import', 'upsert', 'insert', 'save', 'apply',
    'approve', 'reject', 'invite', 'conclude', 'rename', 'bulk',
    # added at p567 from vkumar04/canvas-mcp-lite's author-declared WRITE_TOOLS
    'reply', 'connect', 'comment', 'replace', 'copy', 'hide', 'unhide',
    'lock', 'unlock', 'share', 'subscribe', 'unsubscribe', 'cancel',
    'accept', 'decline',
}
READ_VERB = {
    'get', 'list', 'read', 'fetch', 'search', 'find', 'show', 'view', 'describe',
    'count', 'export', 'download', 'summarize', 'summarise', 'analyze', 'analyse',
    'calculate', 'compute', 'check', 'validate', 'compare', 'preview', 'diff',
    'resolve', 'lookup', 'query', 'inspect', 'report', 'health', 'ping', 'whoami',
}


def tokens(name):
    n = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', name)
    return [t for t in re.split(r'[^A-Za-z0-9]+', n.lower()) if t]


def is_mutating(name):
    tk = tokens(name)
    if not tk:
        return False
    if tk[0] in READ_VERB:
        return False
    if tk[0] in MUT_VERB:
        return True
    # no recognised leading verb: fall back to any mutating token present
    return any(t in MUT_VERB for t in tk)


def scan(path, text, relaxed=False):
    """Return set of tool names declared in one file."""
    names = set()
    lines = text.splitlines()
    n = len(lines)
    for i, line in enumerate(lines):
        win = '\n'.join(lines[i:i + 6])

        if RE_TOOL_LIST.match(line):
            for j in range(i + 1, n):
                if lines[j].lstrip().startswith(']'):
                    break
                m = RE_LIST_REF.match(lines[j])
                if m:
                    names.add(m.group(1).split('.')[-1])
            continue

        if RE_DECOR.search(line):
            m = RE_NAME_KW.search(win)
            if m:
                names.add(m.group(1))
                continue
            for j in range(i, min(i + DEF_WINDOW, n)):
                d = RE_DEF.match(lines[j])
                if d:
                    names.add(d.group(1))
                    break
            continue

        if RE_CALL.search(line):
            tail = line[RE_CALL.search(line).end():]
            m = re.match(r'\s*' + STR, tail)
            if m:
                names.add(m.group(1))
                continue
            m = RE_NAME_KW.search(win)
            if m:
                names.add(m.group(1))
                continue
            for j in range(i + 1, min(i + 4, n)):
                m = RE_FIRST_STR.match(lines[j])
                if m:
                    names.add(m.group(1))
                    break
            continue

        if RE_TOOLCTOR.search(line):
            m = RE_NAME_KW.search(win)
            if m:
                names.add(m.group(1))
                continue

        m = RE_JS_NAME.match(line) or RE_PY_NAME.match(line)
        if m and RE_SPEC_HINT.search(win):
            names.add(m.group(1))
        elif relaxed:
            m = RE_JS_NAME_LOOSE.search(line) or RE_PY_NAME_LOOSE.search(line)
            if m and RE_SPEC_HINT.search(win):
                names.add(m.group(1))
    return names


def walk(root, relaxed=False):
    names, files = set(), 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR]
        for fn in filenames:
            if os.path.splitext(fn)[1] not in SRC_EXT:
                continue
            p = os.path.join(dirpath, fn)
            if RE_TEST_PATH.search(os.path.relpath(p, root).replace(os.sep, '/')):
                continue
            try:
                if os.path.getsize(p) > 2_000_000:
                    continue
                with open(p, 'r', encoding='utf-8', errors='replace') as fh:
                    text = fh.read()
            except OSError:
                continue
            files += 1
            names |= scan(p, text, relaxed)
    return names, files


def main():
    root = sys.argv[1]
    relaxed = '--relaxed' in sys.argv
    names, files = walk(root, relaxed)
    mut = sorted(x for x in names if is_mutating(x))
    out = {
        'root': root,
        'mode': 'relaxed' if relaxed else 'strict',
        'src_files': files,
        'tool_names': len(names),
        'mutating': len(mut),
        'share': round(100.0 * len(mut) / len(names), 1) if names else None,
        'names': sorted(names),
        'mutating_names': mut,
    }
    if '--json' in sys.argv:
        print(json.dumps(out))
    else:
        print(f"{root}\t{files}\t{len(names)}\t{len(mut)}\t{out['share']}")


if __name__ == '__main__':
    main()
