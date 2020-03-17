"""
Created on Mar 17, 2020

@author: Kevin Feng
"""

import sys


def character_mapping(s1, s2):
    """
    check if s1 can be convert to s2 by one-to-one character mapping.
    :param s1: first string
    :param s2: second string
    :return: if first string can be converted to second string return True, else return False
    """
    if len(s1) != len(s2):
        return False
    map_dictionary = {}
    for index, character in enumerate(s1):
        if character in map_dictionary:
            if map_dictionary[character] != s2[index]:
                return False
        else:
            map_dictionary[character] = s2[index]
    return True


if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit("invalid arguments")
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if character_mapping(s1, s2):
        print("true")
    else:
        print("false")
