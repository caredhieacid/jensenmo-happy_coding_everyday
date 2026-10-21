import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from slugkit import slugify


class SlugifyTests(unittest.TestCase):
    def test_words_are_joined_with_hyphens(self):
        self.assertEqual(slugify("Hello World"), "hello-world")

    def test_punctuation_is_dropped(self):
        self.assertEqual(slugify("Ready, set, go!"), "ready-set-go")


if __name__ == "__main__":
    unittest.main()
