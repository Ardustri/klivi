import sys


def get_size(python_object: object) -> int:
    """Return the size of an object."""
    return sys.getsizeof(python_object)
