import os
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from src.slugify import slugify


class TestSlugify(unittest.TestCase):
    def test_acceptance_examples(self):
        self.assertEqual(slugify("Hello World"), "hello-world")
        self.assertEqual(slugify("  A__B   C  "), "a-b-c")
        self.assertEqual(slugify("--Already--Slug--"), "already-slug")
        self.assertEqual(slugify("ABC123"), "abc123")
        self.assertEqual(slugify("***"), "")
        self.assertEqual(slugify(""), "")

    def test_whitespace_and_punctuation_runs(self):
        self.assertEqual(slugify("Hello,   World!"), "hello-world")
        self.assertEqual(slugify("   already-slug   "), "already-slug")
        self.assertEqual(slugify("Alpha---Beta"), "alpha-beta")
        self.assertEqual(slugify("Hello World."), "hello-world")
        self.assertEqual(slugify("#Section 1"), "section-1")

    def test_single_characters(self):
        self.assertEqual(slugify("a"), "a")
        self.assertEqual(slugify("Z"), "z")
        self.assertEqual(slugify("1"), "1")

    def test_alphanumeric_with_underscores_and_numbers(self):
        self.assertEqual(slugify("v1_0_release"), "v1-0-release")
        self.assertEqual(slugify("item-42_test"), "item-42-test")

    def test_no_alphanumeric_remaining(self):
        self.assertEqual(slugify("     "), "")
        self.assertEqual(slugify("---___---"), "")
        self.assertEqual(slugify("!?@#$%^&*()"), "")
        self.assertEqual(slugify(" - - "), "")


if __name__ == "__main__":
    unittest.main()
