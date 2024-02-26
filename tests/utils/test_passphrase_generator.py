from unittest import TestCase

from password_wizard.utils.passphrase_generator import PassphraseGenerator


class TestPassphraseGenerator(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.generator = PassphraseGenerator()

    def test_set_words(self) -> None:
        self.assertEqual(4, self.generator._words)
        self.generator.set_words(6)
        self.assertEqual(6, self.generator._words)

        result = self.generator.generate()
        self.assertNotEqual("", result)

    def test_set_separator(self) -> None:
        self.assertEqual("", self.generator._separator)
        self.generator.set_separator("-")
        self.assertEqual("-", self.generator._separator)

        result = self.generator.generate()
        self.assertNotEqual("", result)
        self.assertIn("-", result)
