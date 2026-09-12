import json
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
EXPORT = ROOT / "exports" / "machine-identities.json"
SCHEMA = ROOT / "contracts" / "machine-identities.schema.json"
FORBIDDEN = {
    "online", "offline", "status", "job", "job_progress", "ready", "readiness",
    "affordances", "schedule", "scheduling",
}


class MachineIdentityContractTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.export = json.loads(EXPORT.read_text())
        cls.schema = json.loads(SCHEMA.read_text())

    def test_contract_is_closed_and_identity_only(self):
        self.assertFalse(self.schema["additionalProperties"])
        self.assertFalse(self.schema["$defs"]["machine"]["additionalProperties"])
        fields = set(self.schema["$defs"]["machine"]["properties"])
        self.assertFalse(fields & FORBIDDEN)

    def test_exported_names_and_aliases_resolve_to_one_machine(self):
        resolved = {}
        for machine in self.export["machines"]:
            for value in [machine["name"], *machine["aliases"]]:
                key = value.casefold()
                self.assertNotIn(key, resolved, f"identity label reused: {value}")
                resolved[key] = machine["id"]
        self.assertEqual(resolved["folgertech i3"], resolved["2020"])
        self.assertEqual(resolved["voxelab aquila"], resolved["aquila x2"])

    def test_existing_consumer_ids_remain_stable(self):
        ids = {machine["name"]: machine["id"] for machine in self.export["machines"]}
        expected = {
            "Bambu Lab P1S": "studio-machine:bambu-p1s",
            "Genmitsu Cubiko": "studio-machine:genmitsu-cubiko",
            "LulzBot Mini 2": "studio-machine:lulzbot-mini-2",
            "Voxelab Aquila": "studio-machine:aquila-modified",
            "FolgerTech i3": "studio-machine:folgertech-i3-rebuild",
        }
        self.assertEqual({name: ids.get(name) for name in expected}, expected)

    def test_every_identity_has_local_provenance(self):
        for machine in self.export["machines"]:
            self.assertTrue(machine["provenance"])
            for evidence in machine["provenance"]:
                source = ROOT / evidence["source"]
                self.assertTrue(source.is_file(), f"missing provenance: {source}")

    def test_export_contains_no_live_operational_fields(self):
        def keys(value):
            if isinstance(value, dict):
                for key, child in value.items():
                    yield key
                    yield from keys(child)
            elif isinstance(value, list):
                for child in value:
                    yield from keys(child)

        self.assertFalse(set(keys(self.export)) & FORBIDDEN)


if __name__ == "__main__":
    unittest.main()
