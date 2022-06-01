'''
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
solution(cell1, cell2) = true.

'''

def solution(cell1, cell2):
    color1 = (ord(cell1[0]) + ord(cell2[0])) % 2 == 0
    color2 = (ord(cell1[1]) + ord(cell2[1])) % 2 == 0
    return color1 == color2
