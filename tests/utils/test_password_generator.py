from unittest import TestCase

from password_wizard.utils.password_generator import PasswordGenerator


class TestPasswordGenerator(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.generator = PasswordGenerator()

    def test_set_length(self) -> None:
        self.assertEqual(len(self.generator.generate()), 18)
        self.generator.set_length(10)
        self.assertEqual(len(self.generator.generate()), 10)

    def test_set_special_characters(self) -> None:
        self.assertIn("_", self.generator._special_chr_list)
        self.assertNotIn("a", self.generator._special_chr_list)
        self.generator.set_special_characters("!#-")
        self.assertIn("!", self.generator._special_chr_list)
        self.assertNotIn("_", self.generator._special_chr_list)

    def test_use_special_characters(self) -> None:
        """Create a separate, seeded version, as not to
        interfere with the class version and accidentally
        break any following tests by using same seed
        """
        _generator = PasswordGenerator()
        _generator.set_seed(0)
        with_symbols = _generator.generate()
        self.assertIn("$", with_symbols)
        _generator.set_use_special_characters(False)
        without_symbols = _generator.generate()
        self.assertNotIn("$", without_symbols)
