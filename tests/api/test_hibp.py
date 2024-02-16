from unittest import TestCase

from password_wizard.api.hibp import HIBP

class TestHIBP(TestCase):
    def test_a(self):
        hibp = HIBP()
        result = hibp.test()
        self.assertTrue(result)
