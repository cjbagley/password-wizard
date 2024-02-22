""" Password Generator - Used to generate a password based on selected options """

import random
import string


class PasswordGenerator:
    """Used to generate a password based on the class attributes:
    - length: the length of the password to set
    - special_char_count: the number of special characters to include
    in the generated password
    """

    def __init__(self) -> None:
        """Default the options for the generated password"""
        self._length = 18
        self._chr_list = string.ascii_letters + string.digits
        self._use_special_chrs = True
        self._special_chr_list = string.punctuation

    def set_length(self, length: int) -> None:
        """Set the length of the generated password"""
        self._length = int(length)

    def set_special_characters(self, chars: str) -> None:
        """Set the list of special chars to use in the password"""
        self._special_chr_list = chars

    def set_use_special_characters(self, should_use: bool) -> None:
        """Do not use any special characters"""
        self._use_special_chrs = bool(should_use)

    def set_seed(self, seed: int = 0) -> None:
        """Set the random seed, to be used when testing"""
        random.seed(seed)

    def generate(self) -> str:
        """Return a randomly generated password
        Uses the class options to determine what the password
        should contain.
        """
        chrs = self._chr_list
        if self._use_special_chrs:
            chrs += self._special_chr_list

        password = ""
        for _ in range(self._length):
            password += random.choice(chrs)

        return password