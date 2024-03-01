"""Check Option - used to compare a given password against 'Have I Been Pwned' list"""

from argparse import Namespace, _SubParsersAction
from getpass import getpass
from password_wizard.cli.options.abstract_option import AbstractOption, ExecuteResult
from password_wizard.utils.utils import sha1_hash
from password_wizard.api.hibp import get_matched_hash_count


class Check(AbstractOption):
    """Subcommand: check
    Parser Options:
        - None
    Execute: Ask the user to enter a password. This password is then
    checked against the 'Have I Been Pwned' records to see if it has
    been leaked, and the amount of times printed to the command line.
    If it has never been leaked, it will show as having been found
    0 times.
    """

    def get_command_name(self) -> str:
        return "check"

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        subparser.add_parser(
            self.get_command_name(),
            help="""Enter a password to see how many times it has been leaked,
            based on data obtained from 'Have I Been Pwned'""",
        )

    def execute(self, args: Namespace) -> ExecuteResult:
        pw = sha1_hash(getpass(prompt="Please enter password to check: "))
        count = get_matched_hash_count(pw)
        return ExecuteResult(
            exit_code=0,
            output=f"This password has been found {count} times",
        )
