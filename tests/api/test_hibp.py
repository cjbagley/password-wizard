from unittest import TestCase
from password_wizard.api.hibp import get_matching_hashes, get_matched_hash_count

HASH_OF_WORD_PASSWORD = "21BD12DC183F740EE76F27B78EB39C8AD972A757"
HASH_OF_OBSCURE_STRING = "77bbf27bed74e01dcb6a250a760f9f463e14bb50"


class TestHIBP(TestCase):
    def test_get_matching_hashes(self):
        # Test errors raised if expected hash not given
        with self.assertRaises(ValueError):
            get_matching_hashes("password")
        with self.assertRaises(ValueError):
            get_matching_hashes("a5af")
        with self.assertRaises(ValueError):
            get_matching_hashes(HASH_OF_OBSCURE_STRING)

        # Test API call works and returns matches
        search_hash = HASH_OF_OBSCURE_STRING[:5]
        self.assertTrue(len(get_matching_hashes(search_hash)) > 700)

    def test_get_matched_hash_count(self):
        # Test errors raised if expected hash not given
        with self.assertRaises(ValueError):
            get_matched_hash_count("password")
        with self.assertRaises(ValueError):
            get_matched_hash_count("123abc")
        with self.assertRaises(ValueError):
            get_matched_hash_count(HASH_OF_OBSCURE_STRING[:5])

        # Check results are as expected
        result = get_matched_hash_count(HASH_OF_WORD_PASSWORD)
        self.assertTrue(result > 0)
        result2 = get_matched_hash_count(HASH_OF_OBSCURE_STRING)
        self.assertTrue(result2 == 0)
