'''
Given an array of integers, replace all the occurrences of elemToReplace with substitutionElem.

Example

For inputArray = [1, 2, 1], elemToReplace = 1, and substitutionElem = 3, the output should be
solution(inputArray, elemToReplace, substitutionElem) = [3, 2, 3].
'''

def solution(inputArray, elemToReplace, substitutionElem):
    op = []
    for x in inputArray:
        if x != elemToReplace: 
            op.append(x)
        else:
            op.append(substitutionElem)
    return op
