#!/usr/bin/python3
""" fill the empty void """


class Rectangle:
    """ defining rectangle """
    number_of_instances = 0
    print_symbol = "#"

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
            void += str(self.print_symbol) * self.__width + "\n"
        void += str(self.print_symbol) * self.__width
        return (void)

    def __repr__(self):
        """EVALLL"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ Here comes the void again """
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if type(rect_1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")

        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1

        return rect_2

    @classmethod
    def square(cls, size=0):

        return cls(size, size)
