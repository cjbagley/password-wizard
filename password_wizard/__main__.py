"""
Main entrypoint for application
Determines if CLI or GUI is being used
"""

from cli import cli


def main() -> None:
    cli.handle()


if __name__ == "__main__":
    main()
