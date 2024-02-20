from unittest import TestCase

from password_wizard.utils.password_generator import PasswordGenerator


class TestPasswordGenerator(TestCase):
    def test_generate(self) -> None:
        generator = PasswordGenerator()
        self.assertEqual(len(generator.generate()), 18)
