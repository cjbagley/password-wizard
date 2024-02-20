""" Password Generator - Used to generate a password based on selected options """


class PasswordGenerator:
    """Used to generate a password based on the class attributes:
    - length: the length of the password to set
    - special_char_count: the number of special characters to include
    in the generated password
    """

    def __init__(self) -> None:
        """Default the options for the generated password"""
        self._length = 18

    def set_length(self, length: int) -> None:
        """Set the length of the generated password"""
        self._length = length

    def generate(self) -> str:
        """Return a randomly generated password
        Uses the class options to determine what the password
        should contain.
        """
        return "password"
