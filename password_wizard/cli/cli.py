""" Handle CLI input to determine what action to take
Options available:
    - check: This will prompt user to input password to check how many times it has been leaked
    - generate: This will randomly generate a password
    - gui: This will open the Password Wizard GUI
"""

import argparse
from types import FunctionType
from getpass import getpass
from utils.utils import sha1_hash
from api.hibp import get_matched_hash_count


def handle():
    parser = argparse.ArgumentParser(description="Password Wizard CLI")
    subparsers = parser.add_subparsers(
        help="Available Password Wizard functionality", title="Actions", required=True
    )

    _check = subparsers.add_parser(
        "check", help="Enter a password to how many times it has been leaked"
    )
    _check.set_defaults(func=check)

    _generate = subparsers.add_parser("generate", help="Generate a password")
    _generate.set_defaults(func=generate)

    _gui = subparsers.add_parser("gui", help="Open the Password Wizard GUI")
    _gui.set_defaults(func=generate)

    args = parser.parse_args()
    if isinstance(args.func, FunctionType):
        args.func(args)


def generate(args):
    print("GENERATE")


def check(args):
    pw = sha1_hash(getpass(prompt="Please enter password to check: "))
    count = get_matched_hash_count(pw)
    print(f"This password has been found {count} times")


def gui(args):
    print("GUI")
