from colorama import Fore, Style, init
from klivi.utils.period import get_current_hour
init(autoreset=True)


def log(log_type, message, fore):
    print(f"{Style.BRIGHT}{fore}[{get_current_hour()}] [{log_type}] {message}")


def info(message):
    log("Info", message, Fore.BLUE)


def warn(message):
    log("Warning", message, Fore.YELLOW)


def error(message):
    log("Error", message, Fore.RED)
    quit()


def succeed(message):
    log("Log", message, Fore.GREEN)


def debug(message):
    log("Debug", message, Fore.MAGENTA)
