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

    def to_json(self):
        """ Json """
        return dict(self.__dict__)
