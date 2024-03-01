"""Passphrase Generator - Used to generate a passphrase"""

import os
import secrets

DEFAULT_WORD_COUNT = 4


class PassphraseGenerator:
    """Generate a passphrase based on the following class attributes:
        - words: the number of words to use in the generated passphrase.
        - separator: character to use between words, if set.
    Example passphrase: HeresAnExamplePassphrase.
    """

    def __init__(self) -> None:
        """Default the options for the generated passphrase"""
        self._word_count = DEFAULT_WORD_COUNT
        self._separator = ""

    def set_word_count(self, words: int) -> None:
        """Set the number of words to use in the generated passphrase"""
        self._word_count = int(words)

    def set_separator(self, separator: str) -> None:
        """Set a separator to use between words"""
        if separator == "":
            self._separator = ""
            return

        self._separator = separator[0]

    def generate(self) -> str:
        """Return a randomly generated passphrase
        Uses the class options to determine what the passphrase
        should contain.
        """
        path = (
            os.path.dirname(os.path.realpath(__file__)) + "/../wordlists/wordlist.txt"
        )
        wordlist = self._get_wordlist(path)
        words = wordlist.lower().split()
        return self._separator.join(
            secrets.choice(words).title() for _ in range(self._word_count)
        )

    def _get_wordlist(self, filepath) -> str:
        """Load wordlist from given file path"""
        with open(file=filepath, mode="r", encoding="utf-8") as f:
            return f.read()
