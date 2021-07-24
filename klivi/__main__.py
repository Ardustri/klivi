import sys

from klivi.lexer import Lexer
from klivi.parser import Parser
from klivi.utils.fs import read_file
from klivi.utils.period import sleep
from klivi.console import Console


def main(file_name):
    source = read_file(file_name)
    lexer = Lexer(source).lexify()
    parser = Parser(lexer)
    parser.render()
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        Console.error("To Few Argument")

    sleep(1)
    Console.info("Starting")
    sleep(1)
    main(sys.argv[1])
    sys.exit(0)
