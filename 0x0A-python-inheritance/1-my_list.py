#!/usr/bin/python3
"""
iherit list
"""


class MyList(list):
    """
    meine nicht sortierte Listenliste
    """
    def print_sorted(self):
        """
        printed sorted list
        """
        print(sorted(self))
