import unittest
from pathlib import Path


ROOT = Path(__file__).parents[1]
PROFILE = ROOT / "templates" / "compute-device-profile-template.md"
GATE_D = ROOT / "personal-machines" / "jetson-compute-candidates" / "gate-d-audit.md"


class ComputeDevicePreparationTest(unittest.TestCase):
    def test_compute_profile_keeps_evidence_kinds_separate(self):
        text = PROFILE.read_text(encoding="utf-8")
        for heading in (
            "## Owner report",
            "## Vendor specification",
            "## Physical inspection",
            "## Benchmark evidence",
            "## Recovery and thermal limits",
        ):
            self.assertIn(heading, text)
        self.assertIn("Do not copy reported values into a verified field", text)

    def test_gate_d_audit_preserves_reported_jetsons_without_identity_claims(self):
        text = GATE_D.read_text(encoding="utf-8")
        self.assertIn("two original NVIDIA Jetson Nano boards, probably 4 GB each", text)
        self.assertIn("one NVIDIA Jetson Orin Nano developer kit, probably 8 GB", text)
        self.assertIn("fan", text)
        self.assertIn("DisplayPort-only", text)
        self.assertIn("USB-C near Ethernet", text)
        self.assertIn("Do not assign an Atlas ID", text)
        self.assertIn("Do not begin an inference workload", text)


if __name__ == "__main__":
    unittest.main()
