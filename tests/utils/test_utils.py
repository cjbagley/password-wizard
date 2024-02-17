from unittest import TestCase
from password_wizard.utils.utils import sha1_hash


class TestUtils(TestCase):
    def test_sha1hash(self):
        expected = "5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"
        result = sha1_hash("password")
        self.assertEqual(result, expected)

        expected = "a94a8fe5ccb19ba61c4c0873d391e987982fbbd3"
        result = sha1_hash("test")
        self.assertEqual(result, expected)
