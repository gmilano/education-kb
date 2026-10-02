#!/usr/bin/env python3
"""Controls for the npm tarball probe (pase 49). No network: the patterns are
what is under test, and a test that needs the registry is not repeatable.

    python3 test_probe.py
"""
import sys

from probe import TOOL_CALL, TOOL_DEF, TOOL_NAME, LICENSE_FILE

CHECKS = []


def ck(label, got, want):
    ok = got == want
    CHECKS.append(ok)
    print("%s %s%s" % ("PASS" if ok else "FAIL", label,
                       "" if ok else "  -> got %r, want %r" % (got, want)))


def names(src):
    return sorted(set(TOOL_NAME.findall(src)) | set(TOOL_DEF.findall(src)))


# -- pattern 1: registerTool("name", ...) -- the current SDK ----------------
ck("registerTool with double quotes",
   names('server.registerTool("sisu_course", {desc: 1})'), ["sisu_course"])
ck("registerTool with single quotes",
   names("server.registerTool('verify_evidence', {"), ["verify_evidence"])
ck("several registerTool calls in one file",
   names("registerTool('a_b', {}) ... registerTool('c_d', {})"),
   ["a_b", "c_d"])

# -- pattern 2: the older getToolDefinitions() array ------------------------
# @imazhar101/mcp-canvas-server is this shape, and it is the reason the first
# version of this probe reported 0 tools for a server exposing 227.
CANVAS = """
export class PageTools {
    getToolDefinitions() {
        return [
            {
                name: 'list_course_pages',
                description: 'List pages in a course',
                inputSchema: {
                    type: 'object',
                    properties: {
                        course_id: { type: 'string', description: 'Course ID' },
                        sort: { type: 'string' },
                    },
                },
            },
            {
                name: 'create_course_page',
                description: 'Create a page',
                inputSchema: { type: 'object', properties: {} },
            },
        ];
    }
}
"""
ck("pattern 2: both tool definitions are found",
   names(CANVAS), ["create_course_page", "list_course_pages"])

# The decisive control: `name:` alone appears on every schema property. Keying
# on `name` ALONE over-counts by an order of magnitude, so a property called
# `name` must NOT become a tool.
SCHEMA_NOISE = """
            {
                name: 'update_user',
                inputSchema: {
                    type: 'object',
                    properties: {
                        name: { type: 'string', description: 'The user name' },
                        short_name: { type: 'string' },
                    },
                },
            },
"""
ck("a schema PROPERTY called 'name' is not counted as a tool",
   names(SCHEMA_NOISE), ["update_user"])
ck("an object with a name and NO inputSchema is not a tool",
   names("{ name: 'just_a_field', description: 'nope' }"), [])
ck("a bare name property is not a tool", names("{ name: 'x' }"), [])

# -- the occurrence/surface distinction ------------------------------------
# @signdocs-brasil/mcp-server ships two builds and registers every tool twice:
# 37 occurrences, 26 distinct tools. Publishing 37 would inflate it by 42 %.
DOUBLE = ("registerTool('create_envelope', {})\n"
          "registerTool('create_envelope', {})\n"
          "registerTool('cancel_envelope', {})\n")
ck("the SURFACE is the distinct-name count",
   len(names(DOUBLE)), 2)
ck("occurrences are counted separately and are higher",
   len(TOOL_CALL.findall(DOUBLE)), 3)

# -- license file detection ------------------------------------------------
for f in ("LICENSE", "LICENSE.md", "LICENCE", "LICENSE.txt", "COPYING",
          "dist/LICENSE"):
    ck("license file recognised: %s" % f, bool(LICENSE_FILE.search(f)), True)
for f in ("README.md", "package.json", "src/license_check.js", "licenses.js"):
    ck("not a license file: %s" % f, bool(LICENSE_FILE.search(f)), False)

print("\n%d/%d checks passed" % (sum(CHECKS), len(CHECKS)))
sys.exit(0 if all(CHECKS) else 1)
