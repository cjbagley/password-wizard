"""Test CLI functionality"""

import re
from unittest import TestCase
from unittest.mock import patch
from password_wizard.cli.options.check import Check
from password_wizard.cli.options.passphrase import Passphrase
from password_wizard.cli.options.password import Password
from password_wizard.cli.cli import get_option_parser


class TestCLI(TestCase):
    """Functionality tests for cli"""

    def test_password(self) -> None:
        """Test password creation CLI argument"""
        option = Password()
        parser = get_option_parser([option])

        # Test CLI with no arguments passed
        args = parser.parse_args([option.get_command_name()])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)

        # Test CLI with arguments passed
        args = parser.parse_args([option.get_command_name(), "-l", "10"])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)
        self.assertTrue(len(output.output) == 10)

        # Test CLI with incorrect arguments passed
        with self.assertRaises(ValueError):
            parser.parse_args([option.get_command_name(), "-non-existing", "10"])

    @patch("password_wizard.cli.options.check.getpass", return_value="password")
    def test_check(self, mock) -> None:  # pylint: disable=unused-argument
        """Test check CLI argument
        Note: mock must be passed in above for mocking to work
        """
        option = Check()
        parser = get_option_parser([option])

        # Test CLI
        args = parser.parse_args([option.get_command_name()])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)
        self.assertIsNotNone(
            re.search("^This password has been found \\d+ times", output.output)
        )

    @patch("password_wizard.cli.options.passphrase.input", return_value="-")
    def test_passphrase(self, mock) -> None:  # pylint: disable=unused-argument
        """Test passphrase generation CLI argument
        Note: mock must be passed in above for mocking to work
        """
        option = Passphrase()
        parser = get_option_parser([option])

        # Test CLI with no arguments passed
        args = parser.parse_args([option.get_command_name()])
        output = option.execute(args)
        self.assertTrue(output.exit_code == 0)

        # Test CLI with arguments passed
        args = parser.parse_args([option.get_command_name(), "-s"])
        output = option.execute(args)

        # Test CLI with incorrect arguments passed
        with self.assertRaises(ValueError):
            parser.parse_args([option.get_command_name(), "-non-existing", "10"])
