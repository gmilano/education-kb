"""The test this project does not have: assert the export gate FIRES when content
credentials are required and the record carries what the pipeline actually puts in it.

`ACTION KR`, p178. Every value here is READ from the subject at
`9c260890214df68ad8fd0d681d3e77a6a7b7ea9f`, never invented:

  * the record shape is the dict returned by `_artifact_provenance`
    (`generation/workflow.py:2520-2534`) -- the ONLY builder of the
    `provenanceRecords` list that `_provenance_quality_gate` reads. 🔴 It has NO
    `c2paStatus` key, so the field the writers store never reaches the reader.
  * `C2paRecord(C2paStatus.NOT_APPLICABLE)` is the constant line `3018` substituted for
    the stored value before edit `4`.
  * `"licensedMedia"` is the literal `origin` written by `licensed_media_workflow.py`
    and `music_workflow.py:159,301`; `OriginKind` spells it `"licensed-media"`, and
    `workflow.py:2515-2516` silently rewrites anything unrecognised to `GENERATED`.

The first test is the CONTROL: it asserts that the UNPATCHED reader lets a record with no
content credentials pass a gate that requires them. A gate fed a constant cannot fail.
"""

from __future__ import annotations

import unittest
from datetime import UTC, datetime

from alystria.security.errors import ValidationError
from alystria.security.gates import ExportGateInput, SecurityGates
from alystria.security.licensing import AssetUse, DistributionPurpose
from alystria.security.provenance import (
    AssetProvenance,
    C2paRecord,
    C2paStatus,
    OriginKind,
    RightsStatus,
)

NOW = datetime(2026, 10, 13, 12, 0, tzinfo=UTC)
HASH = "a" * 64

# `_artifact_provenance`'s output for a licensed stock visual: note that `origin` has
# already been normalised by `workflow.py:2515-2516`, and that there is no `c2paStatus`.
REAL_RECORD = {
    "assetId": "scene-visual:" + HASH[:16],
    "sha256": HASH,
    "role": "scene-visual",
    "origin": "generated",
    "rightsStatus": "verified",
    "licenseId": "CC-BY-4.0",
    "creator": "stock contributor",
    "attribution": "stock contributor",
    "sourceUri": "https://example.invalid/stock/0001",
    "providerId": "stock-search",
    "modelId": "stock-search",
    "modelRevision": "stock-v1",
    "consentIds": [],
}


def _read(value: dict, *, honour_stored: bool) -> AssetProvenance:
    """The reader at `generation/workflow.py:3003-3019`, both sides of edit `4`."""
    c2pa = (
        C2paRecord(C2paStatus(str(value.get("c2paStatus", "absent"))))
        if honour_stored
        else C2paRecord(C2paStatus.NOT_APPLICABLE)
    )
    return AssetProvenance(
        asset_id=str(value["assetId"]),
        sha256=str(value["sha256"]),
        origin=OriginKind(str(value["origin"])),
        rights_status=RightsStatus(str(value["rightsStatus"])),
        license_id=str(value["licenseId"]),
        creator=value.get("creator"),
        attribution=value.get("attribution"),
        source_uri=value.get("sourceUri"),
        provider_id=value.get("providerId"),
        model_id=value.get("modelId"),
        model_revision=value.get("modelRevision"),
        consent_ids=tuple(str(i) for i in value.get("consentIds", [])),
        c2pa=c2pa,
    )


def _gate(asset: AssetProvenance):
    return SecurityGates.export_gate(
        ExportGateInput(
            "export",
            (asset,),
            AssetUse(
                DistributionPurpose.PUBLIC_COMMERCIAL,
                transformed=True,
                attribution_included=True,
            ),
            (),
            (),
            True,
            0,
            True,
            c2pa_required=True,
            evaluated_at=NOW,
        )
    )


class RealRecordMarkingTests(unittest.TestCase):
    def test_control_unpatched_reader_passes_an_unmarked_record(self) -> None:
        # The data loss, on an origin edit 1 does not touch: the record says nothing
        # about credentials, the reader supplies NOT_APPLICABLE, the gate is satisfied.
        asset = _read(dict(REAL_RECORD, origin="licensed-media"), honour_stored=False)
        self.assertEqual(asset.c2pa.status, C2paStatus.NOT_APPLICABLE)
        self.assertTrue(_gate(asset).allowed)

    def test_a_relabelled_stock_asset_cannot_even_be_constructed(self) -> None:
        # Edit 1's real blast radius: `workflow.py:2515-2516` has already rewritten this
        # licensed stock visual's origin to GENERATED, so the pre-edit-4 reader's
        # NOT_APPLICABLE constant is now refused at construction.
        with self.assertRaises(ValidationError):
            _read(REAL_RECORD, honour_stored=False)

    def test_the_builder_never_carries_the_field_the_reader_needs(self) -> None:
        # The whole of edit 4's behaviour rests on this key being absent upstream.
        self.assertNotIn("c2paStatus", REAL_RECORD)

    def test_patched_reader_defaults_to_absent_and_the_gate_fires(self) -> None:
        asset = _read(REAL_RECORD, honour_stored=True)
        self.assertEqual(asset.c2pa.status, C2paStatus.ABSENT)
        decision = _gate(asset)
        self.assertFalse(decision.allowed)
        self.assertIn("export.c2pa", {finding.code for finding in decision.findings})

    def test_the_writers_origin_value_is_not_a_valid_origin_kind(self) -> None:
        # Why a licensed stock photo arrives at the gate labelled GENERATED.
        values = {item.value for item in OriginKind}
        self.assertNotIn("licensedMedia", values)
        self.assertIn("licensed-media", values)

    def test_only_a_signed_manifest_lets_a_generated_asset_export(self) -> None:
        asset = AssetProvenance(
            asset_id="scene-visual:nvidia-flux",
            sha256=HASH,
            origin=OriginKind.GENERATED,
            rights_status=RightsStatus.VERIFIED,
            license_id="Apache-2.0",
            creator="nvidia-nim",
            attribution=None,
            provider_id="nvidia-nim",
            model_id="black-forest-labs/flux.2-klein-4b",
            model_revision="black-forest-labs/flux.2-klein-4b",
            c2pa=C2paRecord(C2paStatus.VALID, HASH, "Alystria", NOW),
        )
        self.assertTrue(_gate(asset).allowed)

    def test_valid_status_without_a_signer_is_structurally_impossible(self) -> None:
        # Why the fix prescribed for the two failing tests could not work as written.
        with self.assertRaises(ValidationError):
            C2paRecord(C2paStatus.VALID)


if __name__ == "__main__":
    unittest.main()
