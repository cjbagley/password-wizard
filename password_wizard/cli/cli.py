""" Handle CLI input to determine what action to take
Options available:
    - check: This will prompt user to input password to check how many times it has been leaked
    - generate: This will randomly generate a password
    - gui: This will open the Password Wizard GUI
"""

import argparse
from cli.options.check import Check
from cli.options.generate import Generate
from cli.options.gui import Gui


def handle() -> None:
    parser = argparse.ArgumentParser(description="Password Wizard CLI")
    subparsers = parser.add_subparsers(
        dest="subparser_name",
        help="Available Password Wizard functionality",
        title="Actions",
        required=True,
    )

    check = Check()
    check.add_sub_parser(subparsers)
    generate = Generate()
    generate.add_sub_parser(subparsers)
    gui = Gui()
    gui.add_sub_parser(subparsers)

    args = parser.parse_args()
    if not hasattr(args, "subparser_name"):
        print("Please enter a valid option - see --help for further details")
        exit(1)

    match args.subparser_name:
        case "check":
            check.execute(args)
        case "generate":
            generate.execute(args)
        case "gui":
            gui.execute(args)
        case _:
            print("Please enter a valid option - see --help for further details")
            exit(1)

    exit(0)
