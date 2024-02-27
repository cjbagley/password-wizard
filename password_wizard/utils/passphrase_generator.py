""" Passphrase Generator - Used to generate a passphrase based on selected options """

import secrets


class PassphraseGenerator:
    """Used to generate a passphrase based on the class attributes:
    - words: the number of words to use
    """

    def __init__(self) -> None:
        """Default the options for the generated passphrase"""
        self._words = 4
        self._separator = ""

    def set_words(self, words: int) -> None:
        """Set the number of words to use in the generated passphrase"""
        self._words = int(words)

    def set_separator(self, separator: str):
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
        wordlist = self.get_wordlist("./../wordlist.txt")
        words = wordlist.lower().split()
        return self._separator.join(
            secrets.choice(words).title() for _ in range(self._words)
        )

    def get_wordlist(self, filepath) -> str:
        """Load wordlist from given filepath"""
        with open(file=filepath, mode="r", encoding="utf-8") as f:
            return f.read()
