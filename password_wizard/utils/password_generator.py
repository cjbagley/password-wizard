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
        self._character_list = string.ascii_letters + string.digits
        self._character_list += string.punctuation

    def set_length(self, length: int) -> None:
        """Set the length of the generated password"""
        self._length = length

    def set_seed(self, seed: int = 0) -> None:
        """Set the random seed, to be used when testing"""
        random.seed(seed)

    def generate(self) -> str:
        """Return a randomly generated password
        Uses the class options to determine what the password
        should contain.
        """
        password = ""
        for _ in range(self._length):
            password += random.choice(self._character_list)

        return password
