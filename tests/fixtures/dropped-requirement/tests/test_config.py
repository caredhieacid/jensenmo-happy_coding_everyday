import unittest
from pathlib import Path

from config import DEFAULTS, load_config

SAMPLE = Path(__file__).resolve().parents[1] / "config.sample.json"


class ConfigTests(unittest.TestCase):
    def test_defaults_apply_when_key_missing(self):
        self.assertEqual(DEFAULTS["retries"], 3)

    def test_sample_config_loads(self):
        config = load_config(SAMPLE)
        self.assertEqual(config["retries"], 5)
        self.assertEqual(config["timeout_seconds"], 30)

    def test_unknown_key_rejected(self):
        import json
        import tempfile

        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as handle:
            json.dump({"retrys": 2}, handle)
        with self.assertRaises(ValueError):
            load_config(handle.name)


if __name__ == "__main__":
    unittest.main()
