"""Tests for utilities"""

from unittest import TestCase
from password_wizard.utils.utils import sha1_hash


class TestUtils(TestCase):
    """Unit tests for utils"""

    def test_sha1hash(self):
        """Test sha1 hash function returns expected values"""
        expected = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
        result = sha1_hash("password")
        self.assertEqual(result, expected)

        expected = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
        result = sha1_hash("test")
        self.assertEqual(result, expected)

        expected = "c036b4e434a3d4b6117e3f609b1d678ff7ff344c"
        result = sha1_hash("LongerStringWithCaps")
        self.assertEqual(result, expected)
