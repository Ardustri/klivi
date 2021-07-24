"""
untilities for common dictionary function
"""
from typing import List, Any, Tuple


def get_keys(dictionary: dict) -> List[Any]:
    return [key for key in dictionary]


def get_value(dictionary: dict) -> List[Any]:
    return [dictionary[key] for key in dictionary]


def dictionary_to_tuple(dictionary: dict) -> List[Tuple[Any]]:
    return [item for item in dictionary.items()]
