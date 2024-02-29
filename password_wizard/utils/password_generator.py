""" Password Generator - Used to generate a password based on selected options """

import secrets
import string

DEFAULT_PASSWORD_LENGTH = 18


class PasswordGenerator:
    """Used to generate a password based on the class attributes:
    - length: the length of the password to set.
    - chr_list: the list of standard characters available
      for random selection in the generated password.
    - use_special_chrs: If True, the password will contain special
      characters.
    - special_chr_list: the list of special characters available
      for random selection in the generated password.
    """

    def __init__(self) -> None:
        """Default the options for the generated password"""
        self._length = DEFAULT_PASSWORD_LENGTH
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
        """Set if any special characters should be selected from"""
        self._use_special_chrs = bool(should_use)

    def generate(self) -> str:
        """Return a randomly generated password
        Uses the class options to determine what the password
        should contain.
        """
        chrs = self._chr_list
        if self._use_special_chrs:
            chrs += self._special_chr_list

        return "".join(secrets.choice(chrs) for _ in range(self._length))
