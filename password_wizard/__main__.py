"""
Main entrypoint for application
Determines if CLI or GUI is being used
"""

from password_wizard.cli import cli

if __name__ == "__main__":
    cli.handle()
