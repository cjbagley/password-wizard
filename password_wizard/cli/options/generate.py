""" Generate Option - used to generate a password """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption


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
        g.add_argument("-x", help="testing", default=2)
        g.add_argument("-y", help="testing", default=3)

    def execute(self, args: Namespace) -> int:
        return 0
