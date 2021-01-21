#!/usr/bin/python3
""" lets read """


def read_file(filename=""):
    """ what to read"""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
