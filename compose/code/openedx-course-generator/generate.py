#!/usr/bin/env python3
"""Open edX course generator — the POST plan for an outline. stdlib only.

Pass 45, action 2 (gap 94). Pass 44 measured the authoring contract of the v1
ViewSet; this turns it into an artifact with a CALL COUNT, which is what goes in
a proposal. Open edX is never started: the plan is computed, then replayed
against a stub that reproduces the three server behaviours measured in the tree.

The contract this is written against, read from openedx/edx-platform @ master
(cms/djangoapps/contentstore/):

  * POST /api/contentstore/v1/xblock/ answers {"locator", "courseKey"} and
    `locator` IS the new block's usage key, so the tree is recursable with no
    extra GET  (xblock_storage_handlers/view_handlers.py:_create_block_core).
  * A child needs its parent's `locator`, so a branch is sequential; siblings
    share a parent and are therefore one parallel wave.
  * Reading the course is ONE call: GET /api/contentstore/v1/course_index/{course_id}
    returns `course_structure`, the nested outline (v1/serializers CourseIndexSerializer).
  * `category` has no enum in a course: XblockSerializer.category is a
    CharField(required=False) with no `choices`. The ["html","problem","video"]
    enum applies only to a LibraryUsageLocator parent.

...and the three ways a malformed body is reported, of which only one is right:

  * no `parent_locator`  -> 403. XblockViewSet.initial() derives course_key from
    the body; HasCourseAuthorAccess.has_permission returns False when it is None.
    A body defect is reported as an authorization failure.
  * no `category`        -> 500. The serializer declares every field
    required=False, so validation passes; then _create_block_core does the bare
    subscript request.json["category"].
  * an unexpected field  -> 400, correctly, because XblockSerializer extends
    StrictSerializer, which rejects extra keys.

So the client validates `parent_locator`, `category` and the field whitelist
BEFORE it emits anything: two of the three server answers would send an operator
to the wrong place.
"""
import json
import os
import sys

CREATE_PATH = "/api/contentstore/v1/xblock/"
COURSE_INDEX_PATH = "/api/contentstore/v1/course_index/{course_id}"
CHILDREN_PATH = "/api/contentstore/v1/container/{usage_key}/children"

# XblockSerializer is a StrictSerializer: any key outside its field set is a 400.
# The create path reads only these four, so the generator sends only these four.
ALLOWED_POST_FIELDS = {"parent_locator", "category", "display_name", "boilerplate"}

# The levels a course outline has. Not an enum the server enforces -- the server
# has none for a course parent -- but the shape a generated course must have.
LEVELS = ("chapter", "sequential", "vertical")
LEAF_CATEGORIES = ("html", "problem", "video", "discussion", "drag-and-drop-v2")


class OutlineError(ValueError):
    """The outline is malformed. Raised by the CLIENT, before any call."""


def _require(node, key, where):
    if key not in node or node[key] in (None, ""):
        raise OutlineError(f"{where}: missing {key!r}")
    return node[key]


def validate_outline(outline):
    """Reject client-side everything the server reports with a wrong status."""
    course_id = _require(outline, "course_id", "outline")
    if not course_id.startswith("course-v1:"):
        raise OutlineError(f"outline: course_id {course_id!r} is not a course-v1 key")

    def walk(nodes, depth, where):
        for i, node in enumerate(nodes):
            at = f"{where}[{i}]"
            category = _require(node, "category", at)
            _require(node, "display_name", at)
            extra = set(node) - {"category", "display_name", "children", "boilerplate"}
            if extra:
                # StrictSerializer would answer 400; say so here instead.
                raise OutlineError(f"{at}: unexpected key(s) {sorted(extra)}")
            expected = LEVELS[depth] if depth < len(LEVELS) else None
            if expected and category != expected:
                raise OutlineError(
                    f"{at}: category {category!r} at depth {depth}, expected {expected!r}")
            if expected is None and category not in LEAF_CATEGORIES:
                raise OutlineError(f"{at}: {category!r} is not a known leaf category")
            kids = node.get("children") or []
            if kids and depth + 1 > len(LEVELS):
                raise OutlineError(f"{at}: a leaf block cannot have children")
            walk(kids, depth + 1, at + ".children")

    walk(outline.get("children") or [], 0, "outline.children")
    return outline


def plan(outline):
    """Return the waves of POSTs, with SYMBOLIC parent references.

    A wave is a set of requests that share no parent-child relation, so they can
    be issued in parallel. Every request in wave n+1 names a parent created in
    wave n, which is the invariant the test asserts. Before the plan runs, no
    locator exists yet, so a parent is referenced as `$<path>` and the executor
    substitutes the real `locator` the POST returned.
    """
    validate_outline(outline)
    waves = []
    frontier = [(outline["course_id"], outline.get("children") or [], "outline")]
    while frontier:
        wave, nxt = [], []
        for parent_ref, kids, path in frontier:
            for i, node in enumerate(kids):
                here = f"{path}.children[{i}]"
                body = {"parent_locator": parent_ref, "category": node["category"],
                        "display_name": node["display_name"]}
                if node.get("boilerplate"):
                    body["boilerplate"] = node["boilerplate"]
                if not set(body) <= ALLOWED_POST_FIELDS:
                    raise OutlineError(
                        f"{here}: body carries {sorted(set(body) - ALLOWED_POST_FIELDS)}, "
                        "which StrictSerializer answers 400")
                wave.append({"method": "POST", "path": CREATE_PATH, "body": body,
                             "ref": f"${here}", "parent_ref": parent_ref})
                if node.get("children"):
                    nxt.append((f"${here}", node["children"], here))
        if wave:
            waves.append(wave)
        frontier = nxt
    return waves


def cost(outline):
    """The number that goes in the proposal: 1 read + 1 POST per block."""
    waves = plan(outline)
    writes = sum(len(w) for w in waves)
    return {"reads": 1, "writes": writes, "calls": 1 + writes,
            "sequential_waves": len(waves),
            "widest_wave": max((len(w) for w in waves), default=0),
            "read_call": COURSE_INDEX_PATH.format(course_id=outline["course_id"])}


def execute(outline, post):
    """Replay the plan. `post(path, body) -> dict` is the transport.

    Emits wave by wave, substituting each parent's real `locator` before the
    children of that parent are sent. Returns (log, locators).
    """
    validate_outline(outline)
    log, locators = [], {}

    def emit(parent_ref, nodes, wave_no):
        """One wave for one parent; returns the children to emit next."""
        created = []
        for node in nodes:
            body = {"parent_locator": parent_ref, "category": node["category"],
                    "display_name": node["display_name"]}
            if node.get("boilerplate"):
                body["boilerplate"] = node["boilerplate"]
            if "parent_locator" not in body or not body["parent_locator"]:
                raise OutlineError("refusing a POST with no parent_locator (server: 403)")
            if "category" not in body or not body["category"]:
                raise OutlineError("refusing a POST with no category (server: 500)")
            res = post(CREATE_PATH, body)
            loc = res["locator"]
            locators[loc] = node["display_name"]
            log.append({"wave": wave_no, "parent": parent_ref, "locator": loc,
                        "category": node["category"]})
            created.append((loc, node.get("children") or []))
        return created

    frontier = [(outline["course_id"], outline.get("children") or [])]
    wave_no = 0
    while frontier:
        nxt = []
        for parent_ref, kids in frontier:
            if kids:
                nxt.extend(emit(parent_ref, kids, wave_no))
        frontier = [(loc, kids) for loc, kids in nxt if kids]
        wave_no += 1
    return log, locators


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "outline.example.json")
    outline = json.load(open(path, encoding="utf-8"))
    c = cost(outline)
    print(f"outline: {path}")
    print(f"read the course : 1 call  -> GET {c['read_call']}")
    print(f"write the course: {c['writes']} calls -> POST {CREATE_PATH}")
    print(f"total           : {c['calls']} calls, in {c['sequential_waves']} sequential waves")
    for i, wave in enumerate(plan(outline)):
        kinds = {}
        for r in wave:
            kinds[r["body"]["category"]] = kinds.get(r["body"]["category"], 0) + 1
        print(f"  wave {i}: {len(wave):3d} POSTs, parallelizable  {kinds}")


if __name__ == "__main__":
    main()
