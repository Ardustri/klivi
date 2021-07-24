import datetime
import time


def get_time():
    return datetime.datetime.now()


def format_time(delimeter, date_format):
    if type(delimeter) != str:
        raise ValueError("Delimeter Should Be String")
    else:
        return get_time().strftime(
            delimeter.join(date_format)
        )


def sleep(second):
    time.sleep(second)


def get_current_hour(delimeter=":", date_format=["%H", "%M", "%S"]):
    return format_time(delimeter, date_format)


def get_current_date(delimeter="/", date_format=["%m", "%d", "%y"]):
    return format_time(delimeter, date_format)


def set_timeout(function, second):
    time.sleep(second)
    function()
