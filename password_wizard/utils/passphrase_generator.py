""" Passphrase Generator - Used to generate a passphrase based on selected options """

import random


class PassphraseGenerator:
    """Used to generate a passphrase based on the class attributes:
    - words: the number of words to use
    """

    def __init__(self) -> None:
        """Default the options for the generated passphrase"""
        self._words = 4

    def set_words(self, words: int) -> None:
        """Set the number of words to use in the generated passphrase"""
        self._words = int(words)

    def set_seed(self, seed: int = 0) -> None:
        """Set the random seed, to be used when testing"""
        random.seed(seed)

    def generate(self) -> str:
        """Return a randomly generated passphrase
        Uses the class options to determine what the passphrase
        should contain.
        """
        return ""
