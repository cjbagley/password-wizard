"""Test Have I Been Pwned API functionality"""

from unittest import TestCase
from password_wizard.api.hibp import _get_matching_hashes, get_matched_hash_count

HASH_OF_WORD_PASSWORD = "21BD12DC183F740EE76F27B78EB39C8AD972A757"  # nosec B105
HASH_OF_OBSCURE_STRING = "77bbf27bed74e01dcb6a250a760f9f463e14bb50"  # nosec B105


class TestHIBP(TestCase):
    """Unit tests for hibp"""

    def test_get_matching_hashes(self):
        """Test that API returns matching hashes"""
        search_hash = HASH_OF_OBSCURE_STRING[:5]
        self.assertTrue(len(_get_matching_hashes(search_hash)) > 700)

        # Test errors raised if expected hash not given
        with self.assertRaises(ValueError):
            _get_matching_hashes("password")
        with self.assertRaises(ValueError):
            _get_matching_hashes("a5af")
        with self.assertRaises(ValueError):
            _get_matching_hashes(HASH_OF_OBSCURE_STRING)

    def test_get_matched_hash_count(self):
        """Test that API returns expected found hash count"""
        result = get_matched_hash_count(HASH_OF_WORD_PASSWORD)
        self.assertTrue(result > 0)
        result2 = get_matched_hash_count(HASH_OF_OBSCURE_STRING)
        self.assertTrue(result2 == 0)

        # Test errors raised if expected hash not given
        with self.assertRaises(ValueError):
            get_matched_hash_count("password")
        with self.assertRaises(ValueError):
            get_matched_hash_count("123abc")
        with self.assertRaises(ValueError):
            get_matched_hash_count(HASH_OF_OBSCURE_STRING[:5])
