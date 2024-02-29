from unittest import TestCase

from password_wizard.utils.passphrase_generator import (
    DEFAULT_WORD_COUNT,
    PassphraseGenerator,
)


class TestPassphraseGenerator(TestCase):
    """Note - no separate test for generate or get_wordlist functions,
    as the below effectively test these anyway
    """

    def test_set_word_count(self) -> None:
        # Test default word count
        generator = PassphraseGenerator()
        self.assertEqual(DEFAULT_WORD_COUNT, generator._word_count)

        # Test a new word count can be set
        generator.set_word_count(6)
        self.assertEqual(6, generator._word_count)

        # Test generate works after new word count set
        result = generator.generate()
        self.assertNotEqual("", result)

    def test_set_separator(self) -> None:
        # Test defaults to no separator
        generator = PassphraseGenerator()
        self.assertEqual("", generator._separator)

        # Test a new separator can be set
        generator.set_separator("-")
        self.assertEqual("-", generator._separator)

        # Test generated passphrase contains new separator
        result = generator.generate()
        self.assertNotEqual("", result)
        self.assertIn("-", result)
