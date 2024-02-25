import re
from unittest import TestCase
from unittest.mock import patch
from password_wizard.cli.options.check import Check
from password_wizard.cli.options.generate_string import GenerateString
from password_wizard.cli.cli import get_option_parser


class TestCLI(TestCase):
    def test_generate_string(self) -> None:
        option = GenerateString()
        parser = get_option_parser([option])

        args = parser.parse_args([option.get_command_name()])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)

        args = parser.parse_args([option.get_command_name(), "-l", "10"])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)
        self.assertTrue(len(output.output) == 10)

        with self.assertRaises(ValueError):
            parser.parse_args([option.get_command_name(), "-not-existing", "10"])

    @patch("password_wizard.cli.options.check.getpass", return_value="password")
    def test_check(self, mock) -> None:
        """Note: mock must be passed in as func arg for mocking purposes, even if not used below"""
        option = Check()
        parser = get_option_parser([option])
        args = parser.parse_args([option.get_command_name()])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)

        self.assertIsNotNone(
            re.search("^This password has been found \\d+ times", output.output)
        )
