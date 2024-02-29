""" Passphrase Option - used to generate a passphrase """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption, ExecuteResult
from password_wizard.utils.passphrase_generator import PassphraseGenerator
from password_wizard.utils.retry import find_non_leaked_password


DEFAULT_WORDS = 4
MAX_WORDS = 8
MIN_WORDS = 3


class Passphrase(AbstractOption):
    """Passphrase Class
    Subcommand: passphrase
    Parser Options:
        -w  - number of words to use
        -s  - separator to use between words
    Execute: Output a passphrase to the command line, based on the selected
    generation options. A passphrase is a password string made from words,
    e.g. "HouseCanTrumpetNose".
    """

    def get_command_name(self) -> str:
        return "passphrase"

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
            help="""Specify a separator between words. No value should be given,
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
            generator.set_word_count(args.words)
        if args.separator:
            separator = self._get_separator_input()
            generator.set_separator(separator)

        return find_non_leaked_password(generator.generate)

    def _get_separator_input(self) -> str:
        """Get special characters to use from user input"""
        return input("Separator to use: ")
