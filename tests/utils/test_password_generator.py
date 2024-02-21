from unittest import TestCase

from password_wizard.utils.password_generator import PasswordGenerator


class TestPasswordGenerator(TestCase):
    def test_set_length(self) -> None:
        generator = PasswordGenerator()
        self.assertEqual(len(generator.generate()), 18)
        generator.set_length(10)
        self.assertEqual(len(generator.generate()), 10)

    def test_set_special_characters(self) -> None:
        generator = PasswordGenerator()
        self.assertIn("_", generator._special_chr_list)
        self.assertNotIn("a", generator._special_chr_list)
        generator.set_special_characters("!#-")
        self.assertIn("!", generator._special_chr_list)
        self.assertNotIn("_", generator._special_chr_list)
