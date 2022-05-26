'''
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
solution(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".


'''

def commonCharacterCount(s1, s2):
    count = 0
    s2_list = list(s2)
    for letter in s1:
        if letter in s2_list:
            s2_list.remove(letter)
            count +=1
            
    return count
  
 
commonCharacterCount("aabcc", "adcaa")
