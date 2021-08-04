from sys import argv
from typing import Dict, Callable

import webview

from klivi.console import Console
from klivi.lexer import Lexer
from klivi.parser import Parser
from klivi.utils.fs import read_file


def run_native(_window_name: str, file_name: str):
    source: str = read_file(file_name)
    lexer: str = Lexer(source).lexify()
    parser: Parser = Parser(lexer)
    parser.render()
    Console.info("Run Native is Coming Soon")
    return True


def run_webview(window_name: str, source: str) -> None:
    webview.create_window(window_name, source)
    webview.start()


class Cli:
    
    def __init__(self, args: argv) -> None:
        self.args: argv = args
        self.commands: Dict[str, Callable[[str, str], None]] = {
            "run_webview": run_webview,
            "run_native": run_native,
        }

    def run(self) -> None:
        if len(self.args) < 2:
            Console.error("To few Argument")
            
        command = self.commands.get(self.args[1])
        
        if command is None:
            Console.error("Command not found.")

        command(argv[2], argv[3])
