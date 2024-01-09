#!/usr/bin/python3
"""Defining BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates a parameter as an integer
        Returns:
        TypeError: if value is not an integer
        ValueError: if value is <= 0
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
