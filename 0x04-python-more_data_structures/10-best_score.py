#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        defi = ""
        score = 0
        for i in a_dictionary:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                defi = i
        return name
    elif a_dictionary is None or len(a_dictionary) == 0:
        return None
