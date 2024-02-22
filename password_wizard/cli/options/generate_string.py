""" Generate Option - used to generate a password """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption
from password_wizard.utils.password_generator import PasswordGenerator


class GenerateString(AbstractOption):
    """Generate Class
    Subcommand: generate
    Parser Options:
        -l - length of password
        -s - what symbol characters to use (default: full punctuation list)
        -ns - do not use special characters, and will override the -s flag
    Execute: Output a password to the command line, based on the selected
    generation options.
    """

    def get_command_name(self) -> str:
        return "generate-string"

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        g = subparser.add_parser(self.get_command_name(), help="Generate a password")
        g.add_argument(
            "-l", help="length of the generated password (default: 18)", default=18
        )
        g.add_argument(
            "-s",
            help="""specify the list of special characters to choose from, for
            example '#!_' (default: full punctuation list)""",
        )
        g.add_argument(
            "-ns",
            help="""do no use any special characters in the password, overriding
            any special characters given with the -s flag""",
            default=True,
            action="store_false",
        )

    def execute(self, args: Namespace) -> int:
        generator = PasswordGenerator()
        if hasattr(args, "l"):
            generator.set_length(args.l)
        if hasattr(args, "s") and args.s is not None:
            generator.set_special_characters(args.s)
        if hasattr(args, "ns") and args.ns is False:
            generator.set_use_special_characters(args.ns)

        print(generator.generate())
        return 0
