from cli.options.abstract_option import AbstractOption
from argparse import Namespace, _SubParsersAction


class Gui(AbstractOption):
    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        subparser.add_parser("gui", help="Open the Password Wizard GUI")

    def execute(self, args: Namespace) -> int:
        return 0
