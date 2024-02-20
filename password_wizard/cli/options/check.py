from cli.options.abstract_option import AbstractOption
from argparse import Namespace, _SubParsersAction
from getpass import getpass
from utils.utils import sha1_hash
from api.hibp import get_matched_hash_count


class Check(AbstractOption):
    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        subparser.add_parser(
            "check", help="Enter a password to how many times it has been leaked"
        )

    def execute(self, args: Namespace) -> int:
        pw = sha1_hash(getpass(prompt="Please enter password to check: "))
        count = get_matched_hash_count(pw)
        print(f"This password has been found {count} times")
        return 0
