"""Tests for passphrase generation"""

from unittest import TestCase

from password_wizard.utils.passphrase_generator import (
    DEFAULT_WORD_COUNT,
    PassphraseGenerator,
)


class TestPassphraseGenerator(TestCase):
    """Unit tests for passphrase_generator"""

    def test_set_word_count(self) -> None:
        """Test word count can be changed"""
        # pylint: disable=protected-access
        generator = PassphraseGenerator()

        # Test default word count
        self.assertEqual(DEFAULT_WORD_COUNT, generator._word_count)

        # Test a new word count can be set
        generator.set_word_count(6)
        self.assertEqual(6, generator._word_count)

        # Test generate works after new word count set
        result = generator.generate()
        self.assertNotEqual("", result)

    def test_set_separator(self) -> None:
        """Test separator can be changed"""
        # pylint: disable=protected-access
        generator = PassphraseGenerator()

        # Test defaults to no separator
        self.assertEqual("", generator._separator)

        # Test a new separator can be set
        generator.set_separator("-")
        self.assertEqual("-", generator._separator)

        # Test generated passphrase contains new separator
        result = generator.generate()
        self.assertNotEqual("", result)
        self.assertIn("-", result)
