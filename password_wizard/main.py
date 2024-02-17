"""
Main entrypoint for module
"""

import sys

from password_wizard.main import main

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(1)
