#!/usr/bin/env python3
"""A stub of POST /api/contentstore/v1/xblock/ — stdlib only.

It is NOT a mock that says yes. It reproduces, as status codes, the four
behaviours read out of openedx/edx-platform @ master, so the generator's
client-side validation is proved against the real contract and not against a
convenience:

  400  an unexpected field            XblockSerializer(StrictSerializer).to_internal_value
  403  no / unparseable parent_locator XblockViewSet.initial + HasCourseAuthorAccess
  500  no category                     _create_block_core: request.json["category"]
  200  {"locator", "courseKey"}        _create_block_core, locator = the new usage key

Synthetic locators have the real shape
`block-v1:<org>+<course>+<run>+type@<category>+block@<32 hex>`, so a client that
parses the locator it gets back is exercised too.
"""
import hashlib

ALLOWED = {"parent_locator", "category", "display_name", "boilerplate"}


class HttpError(Exception):
    def __init__(self, status, body):
        super().__init__(f"{status}: {body}")
        self.status, self.body = status, body


class CreateStub:
    """Counts calls and hands back locators. `calls` is the cost measurement."""

    def __init__(self, course_id):
        self.course_id = course_id
        self.calls = 0
        self.by_status = {}
        self.created = {}        # locator -> (parent_locator, category)

    def _course_parts(self):
        return self.course_id.split("course-v1:", 1)[-1]

    def _record(self, status):
        self.by_status[status] = self.by_status.get(status, 0) + 1

    def post(self, path, body):
        self.calls += 1
        if path != "/api/contentstore/v1/xblock/":
            self._record(404)
            raise HttpError(404, "no such route")

        # 400 — StrictSerializer rejects extra keys. This one the server gets right.
        extra = set(body) - ALLOWED
        if extra:
            self._record(400)
            raise HttpError(400, {f: ["This field is not expected."] for f in sorted(extra)})

        # 403 — initial() could not derive a course_key, so HasCourseAuthorAccess
        # returned False. A malformed body reported as an authorization failure.
        parent = body.get("parent_locator")
        if not parent or not (parent.startswith("course-v1:") or parent.startswith("block-v1:")):
            self._record(403)
            raise HttpError(403, "You do not have permission to perform this action.")
        if parent.startswith("block-v1:") and parent not in self.created:
            self._record(403)
            raise HttpError(403, "unknown parent: course_key could not be derived")

        # 500 — the serializer declares every field optional, so validation passed;
        # then _create_block_core does the bare subscript request.json["category"].
        if "category" not in body or not body["category"]:
            self._record(500)
            raise HttpError(500, "KeyError: 'category'")

        digest = hashlib.md5(
            f"{parent}|{body['category']}|{body.get('display_name')}|{self.calls}".encode()
        ).hexdigest()
        locator = (f"block-v1:{self._course_parts()}+type@{body['category']}"
                   f"+block@{digest}")
        self.created[locator] = (parent, body["category"])
        self._record(200)
        return {"locator": locator, "courseKey": self.course_id}
