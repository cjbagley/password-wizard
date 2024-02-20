""" GUI Option - start the GUI interface """
from argparse import Namespace, _SubParsersAction
from password_wizard.cli.options.abstract_option import AbstractOption


class Gui(AbstractOption):
    """GUI Class
    Subcommand: gui
    Parser Options:
        - None
    Execute: Start the GUI for the user.
    """

    def add_sub_parser(self, subparser: _SubParsersAction) -> None:
        subparser.add_parser("gui", help="Open the Password Wizard GUI")

    def execute(self, args: Namespace) -> int:
        return 0
