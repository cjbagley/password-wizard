from unittest import TestCase
from password_wizard.cli.options.generate_string import GenerateString
from password_wizard.cli.cli import get_option_parser


class TestGenerateString(TestCase):
    def test_generate_string(self) -> None:
        option = GenerateString()
        parser = get_option_parser([option])
        args = parser.parse_args([option.get_command_name(), "-l", "10"])
        output = option.execute(args)
        self.assertTrue(len(str(output)) == 10)
