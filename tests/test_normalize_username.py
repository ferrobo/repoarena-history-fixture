import os
import sys
import unittest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)

from src.normalize_username import normalize_username


class TestNormalizeUsername(unittest.TestCase):
    def test_acceptance_examples(self):
        self.assertEqual(normalize_username(" Alice "), "alice")
        self.assertEqual(normalize_username("USER_123"), "user_123")
        self.assertEqual(normalize_username("A-B_C"), "a-b_c")
        self.assertEqual(normalize_username("a!b@c"), "abc")
        self.assertEqual(normalize_username("***"), "")
        self.assertEqual(normalize_username(""), "")

    def test_whitespace_and_mixed_casing(self):
        self.assertEqual(normalize_username("   LeadingTrailing   "), "leadingtrailing")
        self.assertEqual(normalize_username("\tTabbed\nUser\t"), "tabbeduser")
        self.assertEqual(normalize_username("user name with spaces"), "usernamewithspaces")

    def test_preserved_special_characters(self):
        self.assertEqual(normalize_username("dev-user_01"), "dev-user_01")
        self.assertEqual(normalize_username("---___---"), "---___---")
        self.assertEqual(normalize_username("-_"), "-_")

    def test_removal_of_non_permitted_characters(self):
        self.assertEqual(normalize_username("foo.bar#baz?qux!"), "foobarbazqux")
        self.assertEqual(normalize_username("<user>@domain.com"), "userdomaincom")
        self.assertEqual(normalize_username("100%_valid-id"), "100_valid-id")

    def test_empty_when_no_permitted_characters(self):
        self.assertEqual(normalize_username("   "), "")
        self.assertEqual(normalize_username("!@#$%^&*()+=[]{}|;:',.<>?/~"), "")


if __name__ == "__main__":
    unittest.main()
