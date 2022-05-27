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
    l=len(picture[0])+2
    return ["*"*l]+[x.center(l,"*") for x in picture]+["*"*l]
