""" Generate Option - used to generate a password """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption
from password_wizard.utils.password_generator import PasswordGenerator


class Generate(AbstractOption):
    """Generate Class
    Subcommand: generate
    Parser Options:
        - None
    Execute: Output a password to the command line, based on the selected
    generation options.
    """

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        g = subparser.add_parser("generate", help="Generate a password")
        g.add_argument(
            "-l", help="length of the generated password (default: 18)", default=18
        )
        g.add_argument(
            "-s", help="the number of symbol characters to use (default: 4)", default=4
        )

    def execute(self, args: Namespace) -> int:
        generator = PasswordGenerator()
        print(generator.generate())
        return 0
