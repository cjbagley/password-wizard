from unittest import TestCase

from password_wizard.api.hibp import HIBP

class TestHIBP(TestCase):
    def test_hibp_hash_password(self):
        hibp = HIBP()
        expected = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
        result = hibp.hash("password")
        self.assertEqual(result, expected)

        expected = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
        result = hibp.hash("test")
        self.assertEqual(result, expected)
