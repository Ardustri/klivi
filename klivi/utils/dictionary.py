"""Utilities for common dictionary function."""
from typing import List, Any, Tuple, Dict


def get_keys(dictionary: Dict) -> List[Any]:
    """Return a list of keys in a given dictionary."""
    return list(dictionary.keys())


def get_value(dictionary: Dict) -> List[Any]:
    """Return a list of values in a given dictionary."""
    return list(dictionary.values())


def dictionary_to_tuple(dictionary: Dict) -> List[Tuple[Any, ...]]:
    """Return a tuple from a dictionary."""
    return list(dictionary.items())
