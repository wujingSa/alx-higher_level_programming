#!/usr/bin/python3
"""Defining inherits_from function"""


def inherits_from(obj, a_class):
    """Checks if an object is an inherited instance of a class

    Returns:
    True - if obj is an inherited instance of a_class
    False - Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
