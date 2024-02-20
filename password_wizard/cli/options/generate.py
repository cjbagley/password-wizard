from cli.options.abstract_option import AbstractOption
from argparse import Namespace, _SubParsersAction


class Generate(AbstractOption):
    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        g = subparser.add_parser("generate", help="Generate a password")
        g.add_argument("-x", help="testing", default=2)
        g.add_argument("-y", help="testing", default=3)

    def execute(self, args: Namespace) -> int:
        return 0
