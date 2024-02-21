""" Generate Option - used to generate a password """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption
from password_wizard.utils.password_generator import PasswordGenerator


class Generate(AbstractOption):
    """Generate Class
    Subcommand: generate
    Parser Options:
        -l - length of password
        -s - what symbol characters to use. If not set, use full punctuation list.
    Execute: Output a password to the command line, based on the selected
    generation options.
    """

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        g = subparser.add_parser("generate", help="Generate a password")
        g.add_argument(
            "-l", help="length of the generated password (default: 18)", default=18
        )
        g.add_argument(
            "-s",
            help="""specify the list of special characters to choose from, for example
            '#!_'. If not set, the full punctuation list will be used.""",
        )

    def execute(self, args: Namespace) -> int:
        generator = PasswordGenerator()
        print(generator.generate())
        return 0
