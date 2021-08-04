import sys

from klivi.cli import Cli
from klivi.console import Console


def main() -> bool:
    Cli(sys.argv).run()
    return True


if __name__ == "__main__":
    Console.info("Starting")
    main()
    sys.exit(0)
