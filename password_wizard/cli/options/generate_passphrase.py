""" GeneratePassphrase Option - used to generate a passphrase """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption, ExecuteResult
from password_wizard.utils.passphrase_generator import PassphraseGenerator


DEFAULT_WORDS = 4
MIN_WORDS = 3
MAX_WORDS = 8


class GeneratePassphrase(AbstractOption):
    """GeneratePassphrase Class
    Subcommand: generate-passphrase
    Parser Options:
        -w  - number of words to use
    Execute: Output a passphrase to the command line, based on the selected
    generation options. A passphrase is a password string made from words,
    e.g. "HouseCanTrumpetNose".
    """

    def get_command_name(self) -> str:
        return "generate-passphrase"

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        g = subparser.add_parser(self.get_command_name(), help="Generate a passphrase")
        g.add_argument(
            "-w",
            "--words",
            help=f"""Specify the number of words to use for the generated passphrase. The
            number should be passed along with this option, for example '-w 5'. The number
            must be between {MIN_WORDS} and {MAX_WORDS}.
            (default: {DEFAULT_WORDS})
            """,
            default=DEFAULT_WORDS,
            # Not using below as how argparse displays is not user-friendly
            # choices=range(MIN_WORDS, MAX_WORDS + 1),
            dest="words",
            type=int,
        )
        g.add_argument(
            "-s",
            "--separator",
            help=f"""Specify a separator between words. No value should be given,
            and a separate prompt will appear in which to enter a separator to use.
            The first given separator will be used.
            (default: No separator)
            """,
            default="",
            dest="separator",
            action="store_true",
        )

    def execute(self, args: Namespace) -> ExecuteResult:
        generator = PassphraseGenerator()
        if hasattr(args, "words"):
            if args.words < MIN_WORDS or args.words > MAX_WORDS:
                return ExecuteResult(
                    exit_code=1,
                    output=f"Words specified must be between {MIN_WORDS} and {MAX_WORDS}",
                )
            generator.set_words(args.words)
        if args.separator:
            separator = self.get_separator_input()
            generator.set_separator(separator)
        return ExecuteResult(exit_code=0, output=generator.generate())
    
    def get_separator_input(self) -> str:
        """Get special characters to use from user input"""
        return input("Separator to use: ")
