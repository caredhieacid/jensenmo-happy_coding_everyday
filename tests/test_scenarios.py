import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
SCENARIO_DIR = ROOT / "tests" / "scenarios"
ALLOWED_LANES = {"Everyday", "Collaboration", "Delivery"}


class BehavioralScenarioTests(unittest.TestCase):
    def test_scenarios_are_well_formed_and_unique(self):
        paths = sorted(SCENARIO_DIR.glob("*.json"))
        self.assertGreaterEqual(len(paths), 6)

        seen_ids = set()
        for path in paths:
            with self.subTest(path=path.name):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data["schema_version"], 1)
                self.assertEqual(data["id"], path.stem)
                self.assertNotIn(data["id"], seen_ids)
                seen_ids.add(data["id"])

                self.assertTrue(data["title"].strip())
                self.assertTrue(data["pressure"].strip())
                self.assertTrue(data["prompt"].strip())
                self.assertTrue(set(data["expected_lanes"]).issubset(ALLOWED_LANES))
                self.assertTrue(data["expected_invariants"])
                self.assertTrue(data["forbidden_behaviors"])

    def test_scenario_index_mentions_every_machine_readable_case(self):
        index = (ROOT / "tests" / "scenarios.md").read_text(encoding="utf-8")
        for path in SCENARIO_DIR.glob("*.json"):
            with self.subTest(path=path.name):
                self.assertIn(path.stem, index)


if __name__ == "__main__":
    unittest.main()
