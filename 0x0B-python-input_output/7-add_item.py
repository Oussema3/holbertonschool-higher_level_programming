#!/usr/bin/python3
"""
    a script that adds all arguments to a Python list
"""


from sys import argv
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

name = "add_item.json"

try:
    scripts = load_from_json_file(name)
except:
    with open(name, mode="a") as round:
        scripts = []

for args in argv[1:]:
    scripts.append(args)

save_to_json_file(scripts, name)
