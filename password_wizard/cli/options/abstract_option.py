""" Abstract Option - abstract template for other option classes """
from argparse import Namespace, _SubParsersAction
from abc import ABC, abstractmethod


class AbstractOption(ABC):
    """AbstractOption class, the base for any CLI option classes"""

    @abstractmethod
    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        """Used to dd the option to argparse subparser.
        This should be in form of a single word, for example
        'generate'. Any sub flags for this option can then be
        given as optional arguments, for example '-a'.
        """

    @abstractmethod
    def execute(self, args: Namespace) -> int:
        """Used to perform any actions based on the CLI input
        given by the user.
        """
