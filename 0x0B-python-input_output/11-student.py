#!/usr/bin/python3
""" class Student """


class Student():
    """ Rpresenting a student with:
        first name , last name and age
    """
    def __init__(self, first_name, last_name, age):
        """ class init """
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self, attrs=None):
        """ class init """
        if type(attrs) is list or type(attrs) is tuple:
            round = {}
            for attr in self.__dict__:
                if attr in attrs:
                    round[attr] = self.__dict__[attr]
            return round

        return dict(self.__dict__)

def reload_from_json(self, json):
        """ Replacesattributes """
        self.__dict__.update(json)
