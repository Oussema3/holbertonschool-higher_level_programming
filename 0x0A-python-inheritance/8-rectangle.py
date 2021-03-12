#!/usr/bin/python3
"""
This module contains one class: Rectangle, that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ contains __init__ method """
    def __init__(self, width, height):
        """
        instantiation
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = heigh
