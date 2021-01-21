#!/usr/bin/python3
"""
abt JSON
"""
import json


def load_from_json_file(filename):
    """
    a functiob that create an object from a JSON file
    """
    with open(filename, encoding="utf-8") as round:
        return json.load(round)
