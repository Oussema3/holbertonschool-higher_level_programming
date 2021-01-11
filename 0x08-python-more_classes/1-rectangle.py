#!/usr/bin/python3
""" fill the empty void """


class Rectangle:
    """ defining rectangle """
    def __init__(self, width=0, height=0):
        """ initialize my Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ gzt the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width value """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ get the height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setting the height value """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
