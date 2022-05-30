'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.

'''
def solution(inputString):
    return sum([inputString.count(i)%2 for i in set(inputString)]) <= 1
