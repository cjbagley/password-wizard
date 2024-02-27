from unittest import TestCase

from password_wizard.utils.passphrase_generator import PassphraseGenerator


class TestPassphraseGenerator(TestCase):
    def test_set_words(self) -> None:
        generator = PassphraseGenerator()
        self.assertEqual(4, generator._words)
        generator.set_words(6)
        self.assertEqual(6, generator._words)

        result = generator.generate()
        self.assertNotEqual("", result)

    def test_set_separator(self) -> None:
        generator = PassphraseGenerator()
        self.assertEqual("", generator._separator)
        generator.set_separator("-")
        self.assertEqual("-", generator._separator)

        result = generator.generate()
        self.assertNotEqual("", result)
        self.assertIn("-", result)
