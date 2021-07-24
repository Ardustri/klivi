from colorama import Fore, Style, init
from klivi.utils.period import get_current_hour

init(autoreset=True)


class Console:

    @staticmethod
    def __log(log_type: str, message: str, fore: Fore) -> None:
        """Prints a pretty formatted log message."""
        print(
            f"{Style.BRIGHT}{fore}[{get_current_hour()}] [{log_type}] {message}"
        )
    
    @staticmethod
    def debug(message: str) -> None:
        """Prints a pretty formatted debug log."""
        Console.__log("Debug", message, Fore.MAGENTA)
    
    @staticmethod
    def error(message: str) -> None:
        """Prints a pretty formatted error log and quit to program."""
        Console.__log("Error", message, Fore.RED)
        quit()
    
    @staticmethod
    def info(message: str) -> None:
        """Prints a pretty formatted info log."""
        Console.__log("Info", message, Fore.BLUE)
    
    @staticmethod
    def succeed(message: str) -> None:
        """Prints a pretty formatted succeed log."""
        Console.__log("Log", message, Fore.GREEN)
    
    @staticmethod
    def warn(message: str) -> None:
        """Prints a pretty formatted warn log."""
        Console.__log("Warning", message, Fore.YELLOW)
    

def main():
    lorem = "Lorem ipsum"
    
    Console.debug(lorem)
    Console.info(lorem)
    Console.succeed(lorem)
    Console.warn(lorem)
    
    Console.error(lorem)


if __name__ == '__main__':
    main()
