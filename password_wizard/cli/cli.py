""" Handle CLI input to determine what action to take
Options available:
    - check         Input a password to check how many times it has been leaked
    - passphrase    Generate a passphrase
    - password      Generate a password
"""
import argparse
import sys
from typing import NoReturn
from password_wizard.cli.options.abstract_option import AbstractOption
from password_wizard.cli.options.check import Check
from password_wizard.cli.options.passphrase import Passphrase
from password_wizard.cli.options.password import Password


class ArgumentParser(argparse.ArgumentParser):
    """Custom argument parsing error handling"""

    def error(self, message: str) -> NoReturn:
        raise ValueError(f"Error: {message}")


def get_options() -> list[AbstractOption]:
    """Get a list of the available CLI option classes"""
    return [Check(), Passphrase(), Password()]


def get_option_parser(options: list[AbstractOption]) -> argparse.ArgumentParser:
    """Return a argparse parser based on provided options"""
    parser = ArgumentParser(description="Password Wizard CLI")
    subparsers = parser.add_subparsers(
        dest="subparser_name",
        help="Available Password Wizard functionality",
        title="Actions",
        required=True,
    )
    for opt in options:
        opt.add_sub_parser(subparsers)

    return parser


def handle() -> None:
    """Handle the actions required based on CLI args given"""
    options = get_options()
    parser = get_option_parser(options)
    try:
        args = parser.parse_args()
    except ValueError as e:
        print(e)
        sys.exit(1)

    if not hasattr(args, "subparser_name"):
        print("Please enter a valid option - see --help for further details")
        sys.exit(1)

    for opt in options:
        if opt.get_command_name() == args.subparser_name:
            result = opt.execute(args)
            if result.output:
                print(result.output)
            sys.exit(result.exit_code)

    print("Please enter a valid option - see --help for further details")
    sys.exit(1)
