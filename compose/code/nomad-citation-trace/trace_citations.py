#!/usr/bin/env python3
"""Does project-nomad's retrieval provenance REACH THE STUDENT? -- gap 104.

Pase 48, action 3. P108 promises *"`synthetic` por turno, separando
`direct_source` del resto, 3-4 semanas"* on the strength of ONE reading:
`rag_service.ts` puts `chunk_index` + `source` + `document_id` into the metadata
of a retrieval result. That is the retrieval end. The question action 3 asks is
the other end: does the client receive the identity of the source, or is it
consumed internally for ranking and discarded?

This script answers it by following the value through SEVEN hops of the real
tree, and asserts each one, so the answer survives an upstream change:

    python3 trace_citations.py /path/to/project-nomad

Get the tree with (no blobs, only the paths needed):

    git clone --depth 1 --filter=blob:none --no-checkout \
        https://github.com/Crosstalk-Solutions/project-nomad nomad
    cd nomad && git sparse-checkout init --cone \
      && git sparse-checkout set admin/app admin/types \
             admin/inertia/components/chat admin/database/migrations \
      && git checkout HEAD

github.com answers 403 to curl in this environment and api.github.com denies in
the body (pase 37), so git + raw are the channels. Read from a checkout, never
from a rendered page.
"""
import os
import re
import sys

ok = True
count = 0


def check(label, got, want):
    global ok, count
    count += 1
    good = got == want
    if not good:
        ok = False
    print(f"{'PASS' if good else 'FAIL'}  {label}: got={got!r} want={want!r}")


def read(root, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return None
    return open(path, encoding="utf-8", errors="replace").read()


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    root = os.path.abspath(sys.argv[1])

    rag = read(root, "admin/app/services/rag_service.ts")
    prompt = read(root, "admin/app/utils/rag_prompt.ts")
    chat = read(root, "admin/app/services/chat_service.ts")
    model = read(root, "admin/app/models/chat_message.ts")
    types = read(root, "admin/types/chat.ts")
    bubble = read(root, "admin/inertia/components/chat/ChatMessageBubble.tsx")
    migrations = os.path.join(root, "admin/database/migrations")

    for name, blob in (("rag_service.ts", rag), ("rag_prompt.ts", prompt),
                       ("chat_service.ts", chat), ("chat_message.ts", model),
                       ("types/chat.ts", types), ("ChatMessageBubble.tsx", bubble)):
        check(f"hop source present: {name}", blob is not None, True)
    if not all((rag, prompt, chat, model, types, bubble)):
        print("\nTREE INCOMPLETE -- widen the sparse-checkout and re-run")
        return 1

    print("\n-- hop 1: retrieval EMITS the source identity, not just a score --")
    # The returned metadata object of searchSimilar, at the tail of the method.
    tail = rag[rag.rindex("Return top N results"):][:1400]
    for field in ("source:", "document_id:", "archive_title:", "archive_date:",
                  "chunk_index:"):
        check(f"searchSimilar returns metadata.{field.rstrip(':')}",
              field in tail, True)
    check("and upstream RECORDS that `source` used to be dropped here",
          "previously" in tail and "dropped" in tail, True)

    print("\n-- hop 2: the INJECTED prompt labels each block with its source --")
    check("buildContextBlock exists", "export function buildContextBlock" in prompt, True)
    check("the label carries the title", "[Context ${idx + 1} — ${title}" in prompt, True)
    check("the label deliberately carries NO relevance score",
          "never with the raw relevance score" in prompt, True)

    print("\n-- hop 3: a citation list is built, and from the INJECTED set --")
    check("buildCitations exists", "export function buildCitations" in prompt, True)
    cit = prompt[prompt.index("export function buildCitations"):]
    check("it dedupes on the originating path", "seen.has(key)" in cit, True)
    check("it is fed from what was injected, not from all of retrieval",
          "injected" in prompt, True)
    check("a point with neither path nor title is SKIPPED, not shown as unknown",
          "Unknown source" in prompt, True)

    print("\n-- hop 4: the shape that crosses to the client --")
    m = re.search(r"export interface ChatSource \{(.*?)\}", types, re.S)
    check("ChatSource is declared", bool(m), True)
    fields = sorted(re.findall(r"^\s*(\w+)\??:", m.group(1), re.M)) if m else []
    check("ChatSource fields", fields, ["date", "source", "title"])

    print("\n-- hop 5: it is PERSISTED on the assistant message --")
    check("chat_service stringifies sources into the row",
          "JSON.stringify(sources)" in chat, True)
    check("the model declares the column", "declare sources: string | null" in model, True)
    migs = [f for f in os.listdir(migrations) if "sources_to_chat_messages" in f]
    check("a migration adds the column", len(migs), 1)
    check("the column is nullable text",
          "table.text('sources').nullable()" in read(
              root, f"admin/database/migrations/{migs[0]}"), True)

    print("\n-- hop 6: it is RETURNED to the client --")
    check("history parses it back out", "JSON.parse(msg.sources)" in chat, True)
    check("the fresh reply carries it too",
          "sources: sources && sources.length > 0 ? sources : undefined" in chat, True)

    print("\n-- hop 7: the UI RENDERS it under the assistant answer --")
    check("the bubble renders sources for assistant messages",
          "message.role === 'assistant' && message.sources" in bubble, True)
    check("it maps over them", "message.sources.map(" in bubble, True)

    print("\n-- the LIMIT, which is the part that decides what P108 may promise --")
    check("no per-span boundary crosses to the client (no offsets in ChatSource)",
          [f for f in fields if "offset" in f or "index" in f or "span" in f], [])
    check("no field distinguishes a direct quotation from a synthesis",
          [f for f in fields if f in ("kind", "label", "direct_source",
                                      "synthetic", "verbatim")], [])
    check("citations are deduped per DOCUMENT, so granularity is the document",
          "collapse to one entry" in prompt or "dozen chunks out of one archive"
          in prompt, True)

    print()
    print(f"{count} checks run")
    print("ALL CHECKS PASSED" if ok else "SOME CHECKS FAILED")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
