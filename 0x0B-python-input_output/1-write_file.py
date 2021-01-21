#!/usr/bin/python3
""" Schreiben """


def write_file(filename="", text=""):
    """ bitte schreibe ! """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
