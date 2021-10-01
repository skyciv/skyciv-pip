import copy
import types
from typing import List


def clone(dict: dict) -> dict:
    """Create a deep clone of a dictionary or array.

    Args:
        dict (dict): The dictionary to clone.

    Returns:
        dict: A clone of the input dictionary.
    """
    return copy.deepcopy(dict)


def next_object_key(dict: dict) -> int:
    """Gets next available numerical key in an object starting from 1.

    Args:
        dict (dict): The dictionary of which to get the next available key.

    Returns:
        int: The next a available integer.
    """
    nextKey = 1

    keys = dir(dict)

    while str(nextKey) in keys:
        nextKey += 1

    return nextKey


def has_get_method(dict: dict) -> bool:
    """Check if custom get method is present

    Args:
        dict (dict): The object to check.

    Returns:
        bool: Whether there is a custom get method.
    """
    get_method = getattr(dict, "get", None)
    if callable(get_method):
        if get_method != None and not isinstance(get_method, types.BuiltinFunctionType):
            return True
    return False


def keyvals(obj: dict) -> List[list]:
    """Return the key value pairs of a class or dictionary.
    Args:
        obj (dict): A class or dictionary.

    Returns:
        list[list]: An array of keyvalue pairs
    """

    if type(obj) is dict:
        return obj.items()
    else:
        return vars(obj).items()


def keys(obj: dict) -> List[list]:
    """Return the keys of a class or dictionary.
    Args:
        obj (dict): A class or dictionary.

    Returns:
        list[list]: An array of keys
    """

    if type(obj) is dict:
        return obj.keys()
    else:
        return vars(obj).keys()
