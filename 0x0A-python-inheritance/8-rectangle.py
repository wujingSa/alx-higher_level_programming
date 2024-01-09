#!/usr/bin/python3
"""Defining Rectangle class that inherits from BaseGeometry class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""

    def __init__(self, width, height):
        """intializes a new Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self. integer_validator("height", height)
        self.__height = height
