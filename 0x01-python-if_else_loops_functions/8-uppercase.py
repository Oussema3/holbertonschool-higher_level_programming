#!/usr/bin/python3
def uppercase(str):
    result = ""
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for i in str:
        if i not in alphabet or alphabet.index(i) >= 26:
            result += i
        else:
            result += alphabet[alphabet.index(i)+26]
        
    print(result)
