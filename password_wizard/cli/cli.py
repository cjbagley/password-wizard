""" Handle CLI input to determine what action to take
Options available:
    - check: This will prompt user to input password to check how many times it has been leaked
    - generate: This will randomly generate a password
    - gui: This will open the Password Wizard GUI
"""
import argparse
import sys
from password_wizard.cli.options.abstract_option import AbstractOption
from password_wizard.cli.options.check import Check
from password_wizard.cli.options.generate_string import GenerateString
from password_wizard.cli.options.gui import Gui

def get_options() -> list[AbstractOption]:
    """Get a list of the available CLI option classes"""
    return [Check(), GenerateString(), Gui()]

def parse_option_args(options: list[AbstractOption]) -> argparse.Namespace:
    """Parse CLI input based on provided options"""
    parser = argparse.ArgumentParser(description="Password Wizard CLI")
    subparsers = parser.add_subparsers(
        dest="subparser_name",
        help="Available Password Wizard functionality",
        title="Actions",
        required=True,
    )
    for opt in options:
        opt.add_sub_parser(subparsers)

    return parser.parse_args()


def handle() -> None:
    """Handle the actions required based on CLI args given"""
    options = get_options()
    args = parse_option_args(options) 
    
    if not hasattr(args, "subparser_name"):
        print("Please enter a valid option - see --help for further details")
        sys.exit(1)

    for opt in options:
        if opt.get_command_name() == args.subparser_name:
            exit_code: int = opt.execute(args)
            sys.exit(exit_code)

    print("Please enter a valid option - see --help for further details")
    sys.exit(1)
