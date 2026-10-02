#!/usr/bin/env python3
"""Article 50(2) marking for educational generative output -- pass 46, action 1
(gap 95).

Pass 45 measured the hole: 32 of the 66 rows of ../../agents/top.md put synthetic
content in front of a student or a teacher, and 0 of 33 repos can mark it. It
also found that the three pieces needed already exist in this KB and only had to
be joined:

  * the FIELD and the TRANSPORT -- zijinz456/OpenTutor (MIT). `build_provenance`
    emits {"generated": true, "source_labels": [... "generated"]} and
    routers/chat.py:214 serves it to the client. It marks the TURN.
  * the LABEL and the PER-CLAIM GRANULARITY -- JuneYaooo/lineage-skill
    (Apache-2.0), references/provenance-policy.md: a closed vocabulary of 9
    values required for "every consequential claim, task answer, rubric rule,
    feedback judgment, and Personal Skill rule". It has no boolean and no
    transport.
  * the SIGNATURE -- the permissive forensic layer (MarkLLM / SynthID-Text,
    Apache-2.0, P33). NOT implemented here: see `sign_hook` below, which is a
    documented seam and says so.

This module is the join. It takes lineage-skill's labels, decides the boolean
that nobody had decided, and emits OpenTutor's payload extended to the SPAN.

Pure stdlib. No dependency on either upstream project at runtime: the vocabulary
is transcribed from the policy file and asserted against it in test_marking.py.
"""
from __future__ import annotations

import json
from typing import Any, Iterable

# --------------------------------------------------------------------------
# The decision this module exists to make.
# --------------------------------------------------------------------------
# lineage-skill publishes 9 provenance values and NO boolean. Article 50(2) needs
# a boolean: is this text machine-generated? Mapping one to the other is a design
# decision, and pass 45 recorded that nobody had taken it. Here it is, with the
# reason per value, because a reviewer will ask about exactly two of them.
#
# The rule: `synthetic` is True when the MODEL authored the words. Not "is it
# true", not "is it well sourced" -- those are different axes, and conflating
# them is how this field gets filled in wrong.
PROVENANCE_SYNTHETIC: dict[str, bool] = {
    # Authored by the teacher's source material; the model is quoting, not writing.
    "direct_source": False,
    # Authored by the model, even though every input was the teacher's. "Bounded
    # synthesis" is still synthesis: the sentences are the model's.
    "source_grounded_synthesis": True,
    "cross_source_synthesis": True,
    # "runtime interpretation not stated by the teacher" -- the model's own words
    # by definition. The clearest True in the vocabulary.
    "mentor_inference": True,
    # Authored by the LEARNER, a human. Marking these as AI-generated would be
    # wrong in the direction that matters most: it would tell a student their own
    # sentence was written by a machine.
    "learner_hypothesis": False,
    "learner_observation": False,
    # An observed project, metric, expert or experiment result: a human-world
    # fact carried through, not generated.
    "real_world_evidence": False,
    # "knowledge outside the packaged teacher sources" -- it came out of the
    # model's weights. Nothing else could have supplied it.
    "external_general_knowledge": True,
    # 🔵 THE ONE GENUINE JUDGEMENT CALL, and it goes against the count pass 45
    # wrote down. Pass 45 said "4 of the 9 values are literally 'the model
    # produced this'", naming the four above. `unsupported` -- "no adequate
    # evidence is available" -- is about EVIDENCE, not authorship, so it reads
    # like a fifth category rather than a fifth True.
    #
    # It is marked True anyway, and the reason is that the alternative is worse.
    # If no source supports the claim, no source WROTE it either; the only
    # remaining author is the model. Marking it False would create the one
    # failure mode Article 50(2) exists to prevent: unsourced model prose
    # reaching a student with `synthetic: false` attached. So this mapping has
    # FIVE synthetic values, not four, and the extra one is deliberate.
    "unsupported": True,
}

#: Exactly the 9 values of references/provenance-policy.md, in its order.
VOCABULARY: tuple[str, ...] = tuple(PROVENANCE_SYNTHETIC)

#: Emitted beside `provenance` when a label is not in the closed vocabulary.
UNKNOWN_LABEL = "unknown_provenance"


class ProvenanceError(ValueError):
    """Raised when a span cannot be marked at all."""


def is_synthetic(provenance: str) -> bool:
    """Map one lineage-skill label to the Article 50(2) boolean.

    Fails CLOSED: an unrecognised label is synthetic. A vocabulary that grows
    upstream must not silently start emitting `synthetic: false`.
    """
    if not isinstance(provenance, str) or not provenance:
        raise ProvenanceError("provenance label must be a non-empty string")
    return PROVENANCE_SYNTHETIC.get(provenance, True)


def mark_span(
    *,
    text: str,
    provenance: str,
    start: int | None = None,
    end: int | None = None,
    source_ref: str | None = None,
) -> dict[str, Any]:
    """One marked span: the boolean, the ORIGINAL label, and the offsets.

    Keeping the original label beside the boolean is the whole point of not
    collapsing the vocabulary. `synthetic` answers the regulator; `provenance`
    answers the teacher who wants to know WHY, and survives a vocabulary that
    gains a tenth value.
    """
    if not isinstance(text, str):
        raise ProvenanceError("span text must be a string")
    synthetic = is_synthetic(provenance)
    span: dict[str, Any] = {
        "text": text,
        "provenance": provenance,
        "synthetic": synthetic,
        "start": 0 if start is None else int(start),
        "end": (len(text) if end is None else int(end)),
    }
    if provenance not in PROVENANCE_SYNTHETIC:
        span["flags"] = [UNKNOWN_LABEL]
    if source_ref:
        span["source_ref"] = source_ref
    return span


def spans_from_segments(segments: Iterable[tuple[str, str]]) -> list[dict[str, Any]]:
    """Build contiguous spans from (text, provenance) pairs, computing offsets.

    This is the shape a turn pipeline actually has: a list of chunks it knows the
    origin of. Offsets are over the concatenation, so they index the delivered
    text and stay valid when the artifact is detached from the envelope.
    """
    out: list[dict[str, Any]] = []
    cursor = 0
    for text, provenance in segments:
        out.append(mark_span(
            text=text, provenance=provenance, start=cursor, end=cursor + len(text)
        ))
        cursor += len(text)
    return out


def sign_hook(artifact: dict[str, Any]) -> dict[str, Any]:
    """SEAM, not an implementation. Returns `artifact` unchanged.

    The in-artifact signature (MarkLLM / SynthID-Text, Apache-2.0, P33) is a
    watermark over the generated TOKENS, which needs the decoder. This module
    runs after decoding, so it cannot produce one and does not pretend to: it
    records where the call goes and what it would cover.

    🔴 Until this seam is filled, the limit pass 45 named still holds: the mark
    is a field BESIDE the text, not IN it. Copy the text out and the mark is
    gone. `detach_artifact` below narrows that -- it keeps the mark attached to
    the text through a serialisation boundary -- but it is not a watermark, and
    calling it one would be the kind of wrong data this KB keeps correcting.
    """
    return artifact


def build_marked_provenance(
    *,
    spans: list[dict[str, Any]],
    scene: str | None = None,
    workflow: str | None = None,
    source_labels: list[str] | None = None,
    extra: dict[str, Any] | None = None,
) -> dict[str, Any]:
    """OpenTutor's payload shape, extended to the span.

    Compatible on purpose: `generated` and `source_labels` keep the meaning
    routers/chat.py:214 already serves and schemas/task.py:59 already persists,
    so a consumer that only knows the turn-level field keeps working. What is new
    is `spans`, `synthetic_span_count` and `synthetic_char_count`.

    `generated` is the OR over the spans: a turn with one synthetic span is a
    turn containing machine-generated content. Note this is STRICTER than
    OpenTutor, whose turn_pipeline hard-codes generated=True on the agent path --
    here a turn that only quotes sources and relays learner words reports False,
    and reports it because it was measured span by span rather than assumed.
    """
    if not isinstance(spans, list):
        raise ProvenanceError("spans must be a list")
    synth = [s for s in spans if s.get("synthetic")]
    labels = list(source_labels or [])

    generated = bool(synth)
    if workflow and "workflow" not in labels:
        labels.append("workflow")
    if generated and "generated" not in labels:
        labels.append("generated")

    payload: dict[str, Any] = {
        "scene": scene,
        "workflow": workflow,
        "source_labels": labels,
        # --- the turn-level contract OpenTutor already has ---
        "generated": generated,
        # --- the per-span extension this module adds ---
        "spans": spans,
        "span_count": len(spans),
        "synthetic_span_count": len(synth),
        "synthetic_char_count": sum(
            max(0, int(s.get("end", 0)) - int(s.get("start", 0))) for s in synth
        ),
        "provenance_vocabulary": "lineage-skill/references/provenance-policy.md",
        "marking_profile": "aiact-50-2/span/v1",
    }
    if extra:
        payload.update(extra)
    return sign_hook(payload)


def detach_artifact(payload: dict[str, Any]) -> dict[str, Any]:
    """The artifact ALONE: delivered text plus its marks, no envelope.

    This is the object that gets exported, packaged into SCORM, or written to a
    file -- the moment where a mark living only in the transport envelope would
    be lost. Everything needed to re-read the marking travels inside it.
    """
    spans = payload.get("spans") or []
    return {
        "marking_profile": payload.get("marking_profile"),
        "text": "".join(s.get("text", "") for s in spans),
        "generated": bool(payload.get("generated")),
        "spans": [
            {
                "start": s.get("start"),
                "end": s.get("end"),
                "provenance": s.get("provenance"),
                "synthetic": s.get("synthetic"),
            }
            for s in spans
        ],
    }


def synthetic_ranges(artifact: dict[str, Any]) -> list[tuple[int, int]]:
    """The (start, end) ranges a reader must disclose as machine-generated."""
    return [
        (int(s["start"]), int(s["end"]))
        for s in (artifact.get("spans") or [])
        if s.get("synthetic")
    ]


def round_trip(artifact: dict[str, Any]) -> dict[str, Any]:
    """json.dumps -> json.loads, the boundary assertion 3 of action 1 names."""
    return json.loads(json.dumps(artifact, ensure_ascii=False))


# --------------------------------------------------------------------------
# The SCORM injection point, measured in pass 46 action 3 (gap 97).
# --------------------------------------------------------------------------
#: Namespace for the marker inside imsmanifest.xml's <metadata>.
#: 🔴 It MUST be a foreign namespace. Measured with xmllint against the bundled
#: imscp_v1p1.xsd: a namespaced element inside <metadata> VALIDATES (metadataType
#: ends in grp.any -> xsd:any namespace="##other" processContents="lax"
#: maxOccurs="unbounded"), while an element in the default namespace FAILS.
MANIFEST_NS = "urn:globant:aiact:50-2"


def manifest_metadata_fragment(artifact: dict[str, Any]) -> str:
    """The XML to splice into <metadata> of imsmanifest.xml.

    Injected ONCE at packaging rather than in each of the 32 generators -- the
    decision action 3 was written to make, and it came back in favour.
    """
    ranges = synthetic_ranges(artifact)
    rows = "".join(
        '\n      <m:span start="%d" end="%d"/>' % (a, b) for a, b in ranges
    )
    return (
        '<m:aiGenerated xmlns:m="%s" value="%s" profile="%s">%s\n    </m:aiGenerated>'
        % (
            MANIFEST_NS,
            "true" if artifact.get("generated") else "false",
            artifact.get("marking_profile") or "aiact-50-2/span/v1",
            rows,
        )
    )
