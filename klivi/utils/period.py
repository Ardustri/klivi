import datetime
import time
from typing import List, Union, Tuple, Callable, Any


def get_time():
    return datetime.datetime.now()


def format_time(
        delimiter: str,
        date_format: Union[Tuple[str], List[str]]
) -> str:
    """Format time to a human-readable string."""
    if not isinstance(delimiter, str):
        raise ValueError("Delimiter Should Be String")
        
    return get_time().strftime(delimiter.join(date_format))


def sleep(second: int) -> None:
    """Sleeps a given number of seconds."""
    time.sleep(second)


def get_current_hour(delimiter=":", date_format=None):
    """Return a pretty formatted string of the current hour."""
    if date_format is None:
        date_format = ("%H", "%M", "%S")
        
    return format_time(delimiter, date_format)


def get_current_date(delimiter="/", date_format=None):
    """Return a pretty formatted of the current date."""
    if date_format is None:
        date_format = ("%m", "%d", "%y")
        
    return format_time(delimiter, date_format)


def set_timeout(function: Callable[[], Any], second: int) -> Any:
    """Runs a given function after a given number of seconds."""
    time.sleep(second)
    return function()
