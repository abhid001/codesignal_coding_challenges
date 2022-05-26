'''
Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
  solution(inputString) = true;
For inputString = "abac", the output should be
  solution(inputString) = false;
For inputString = "a", the output should be
  solution(inputString) = true.
'''

def checkPalindrome(inputString):
    if inputString == inputString[::-1]:
        return True
    else:
        return False
        
checkPalindrome("aabaa")
