'''
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

Example

For inputArray = [3, 6, -2, -5, 7, 3], the output should be
solution(inputArray) = 21.

7 and 3 produce the largest product.
'''

def solution(inputArray):
    curr_max = inputArray[0] * inputArray[1]
    n = len(inputArray)
    for i in range(0, n-1):
        j = i + 1
        curr_max = max(inputArray[i] * inputArray[j], curr_max)  
  return   curr_max     
    
''' 
Input:  inputArray: [3, 6, -2, -5, 7, 3]
Expected Output: 21
'''
