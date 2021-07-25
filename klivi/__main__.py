import sys

from klivi.lexer import Lexer
from klivi.parser import Parser
from klivi.utils.fs import read_file
from klivi.utils.period import sleep
from klivi.console import Console
from klivi.cli import Cli


def main() -> bool:
    Cli(sys.argv).run()
    return True


if __name__ == "__main__":
    Console.info("Starting")
    main()
    sys.exit(0)
