""" Abstract Option - abstract template for other option classes """
from argparse import Namespace, _SubParsersAction
from abc import ABC, abstractmethod
from collections import namedtuple

ExecuteResult = namedtuple("ExecuteResult", ["exit_code", "output"])


class AbstractOption(ABC):
    """AbstractOption class, the base for any CLI option classes"""

    @abstractmethod
    def get_command_name(self) -> str:
        """Used to get the command name to use for this option
        This should be a single string, with no prefix, that
        describes the action the option will take, for example:
        'check' or 'generate-string'.
        """

    @abstractmethod
    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        """Used to add this option to argparse subparser.
        First, the command name needs to be set with:
        g = subparser.add_parser(self.get_command_name(), help="...")
        Any sub flags for this option can then be
        given as optional arguments, for example:
        g.add_argument("-a", help="...")
        """

    @abstractmethod
    def execute(self, args: Namespace) -> ExecuteResult:
        """Used to perform any actions based on the CLI input
        given by the user. Returns the results in the form
        of a named tuple.
        """
