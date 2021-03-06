'''
After they became famous, the CodeBots all decided to move to a new building and live together. The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains an integer that represents the price of the room. Some rooms are free (their cost is 0), but that’s probably because they are haunted, so all the bots are afraid of them. That is why any room that is free or is located anywhere below a free room in the same column is not considered suitable for the bots to live in.

Help the bots calculate the total price of all the rooms that are suitable for them.

Example

For
matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]
the output should be matrixElementsSum(matrix) = 9.

Input/Output

[execution time limit] 4 seconds (py3)

[input] array.array.integer matrix

A 2-dimensional array of integers representing a rectangular matrix of the building.

Guaranteed constraints: 1 ≤ matrix.length ≤ 5, 1 ≤ matrix[i].length ≤ 5, 0 ≤ matrix[i][j] ≤ 10.

[output] integer

The total price of all the rooms that are suitable for the CodeBots to live in.
'''

def matrixElementsSum(matrix):
    sum_matrix = 0
    
    haunted_room = list()
    for i in range(0, len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                haunted_room.append(j)
        for k in range(len(matrix[0])):
            if k not in haunted_room:
                sum_matrix += matrix[i][k]

    return sum_matrix
