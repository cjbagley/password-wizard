from unittest import TestCase
from password_wizard.api.hibp import getResults

class TestHIBP(TestCase):
    def test_get_results(self):
        results = getResults("password")
        self.assertTrue(len(results) > 700)
