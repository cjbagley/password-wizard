from unittest import TestCase
from password_wizard.api.hibp import get_matching_hashes


class TestHIBP(TestCase):
    def test_get_matching_hashes(self):
        with self.assertRaises(ValueError):
            get_matching_hashes("password")
        with self.assertRaises(ValueError):
            get_matching_hashes("pass")
        self.assertTrue(len(get_matching_hashes("5baa6")) > 700)
