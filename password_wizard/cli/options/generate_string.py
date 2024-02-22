""" GenerateString Option - used to generate a password """
import string
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption
from password_wizard.utils.password_generator import PasswordGenerator


DEFAULT_LENGTH = 18
MIN_LENGTH = 5
MAX_LENGTH = 20
PUNCTUATION = string.punctuation.replace("%", "%%")


class GenerateString(AbstractOption):
    """GenerateString Class
    Subcommand: generate-string
    Parser Options:
        -l  - length of password
        -s  - what symbol characters to use (default: full punctuation list)
        -ns - do not use special characters, and will override the -s flag
    Execute: Output a password to the command line, based on the selected
    generation options.
    """

    def get_command_name(self) -> str:
        return "generate-string"

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        g = subparser.add_parser(self.get_command_name(), help="Generate a password")
        g.add_argument(
            "-l",
            "--length",
            help=f"""Specify a length for the generated password. The length should be
            a number passed along with this option, for example '-l 20'. The number
            must be between {MIN_LENGTH} and {MAX_LENGTH}.
            (default: {DEFAULT_LENGTH})
            """,
            default=DEFAULT_LENGTH,
            # Not using below as how argparse displays is not user-friendly
            # choices=range(MIN_LENGTH, MAX_LENGTH + 1),
            dest="length",
            type=int,
        )
        g.add_argument(
            "-s",
            help=f"""By default, a full punctuation list is used when generating the
            random string. To use only a set selection of special characters, e.g. only use a 
            special character from one of w '#!_', this flag can be set. No value should be given,
            and a separate prompt will appear in which to enter the special characters to use.
            (default: {PUNCTUATION})
            """,
            dest="special_chars",
            action="store_true",
        )
        g.add_argument(
            "-ns",
            help="""By default, special characters will be included in the generated password.
            To exclude any special characters from being used, this flag can be set. No option
            value should be given, and this option will override any other special character
            related options.
            """,
            default=True,
            dest="no_special_chars",
            action="store_false",
        )

    def execute(self, args: Namespace) -> int:
        generator = PasswordGenerator()
        if hasattr(args, "length"):
            if args.length < MIN_LENGTH or args.length > MAX_LENGTH:
                print(f"Length specified must be between {MIN_LENGTH} and {MAX_LENGTH}")
                return 1
            generator.set_length(args.length)
        if args.special_chars:
            chars = self.get_special_char_input()
            generator.set_special_characters(chars)
        if args.no_special_chars is False:
            generator.set_use_special_characters(args.no_special_chars)

        print(generator.generate())
        return 0

    def get_special_char_input(self) -> str:
        """Get special characters to use from user input"""
        chars = set()
        for c in input("Special characters to use: "):
            if c in PUNCTUATION:
                chars.add(c)
        return "".join(chars)
