#!/usr/bin/python3
"""
JSON
"""
import json


def save_to_json_file(my_obj, filename):
    """
     a function that writes an Object to a text file, using a JSON representation:
    """
    with open(filename, mode='w', encoding="utf-8") as round:
        json.dump(my_obj, round)
