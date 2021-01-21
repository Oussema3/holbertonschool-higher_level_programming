#!/usr/bin/python3
""" Module implementing class Student """


class Student():
    """ Rpresenting a student with:
        first_name,last_name and age 
    """

    def __init__(self, first_name, last_name, age):
        """ class init  """
        self.first_name = first_name
        self.age = age
        self.last_name = last_name

    def to_json(self, attrs=None):
        """ Returning dictionary representation
        """
        if attrs and type(attrs) is list:
            round = {}
            for attr in self.__dict__:
                if attr in attrs:
                    round[attr] = self.__dict__[attr]
            return round

        return dict(self.__dict__)

    def reload_from_json(self, json):
        """ Replaces all attributes """
        self.__dict__.update(json)
