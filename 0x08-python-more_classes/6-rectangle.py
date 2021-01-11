#!/usr/bin/python3
""" fill the empty void """


class Rectangle:
    """ defining rectangle """
    def __init__(self, width=0, height=0):
        """ initialize my Rectangle"""
        
        self.width = width
        self.height = height
        type(self).number_of_instances += 1
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
        """ sett the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ get the area of the Rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ get the perimeter of the Rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        void = ""
        if self.__width == 0 or self.__height == 0:
            return (void)
        for i in range(self.__height - 1):
            void += "#" * self.__width + "\n"
        void += "#" * self.__width
        return (void)

    def __repr__(self):
        """EVALLL"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ bitte mir sagen das ist nicht die ende HAHAHAHA """
        print("Bye rectangle...")
        type(self).number_of_instances += 1
