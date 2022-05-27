'''
Given a rectangular matrix of characters, add a border of asterisks(*) to it.

Example

For

picture = ["abc",
           "ded"]
the output should be

solution(picture) = ["*****",
                      "*abc*",
                      "*ded*",
                      "*****"]
'''

def solution(picture):
    picture = ["*" + string + "*" for string in picture]
    print(picture)
    picture = [("*" * len(picture[0]))] + picture + [("*" * len(picture[0]))]
    print(picture)
    return picture
