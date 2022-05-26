'''
Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky if the sum of the first half of the digits is equal to the sum of the second half.

Given a ticket number n, determine if it's lucky or not.

Example:

For n = 1230, the output should be
  solution(n) = true;
For n = 239017, the output should be
  solution(n) = false.

'''

def isLucky(n):
    string = str(n)
    first_half = [int(x) for x in string[:len(string)//2]]
    second_half = [int(x) for x in string[len(string)//2:]]
    return sum(first_half) == sum(second_half)
  
  
 isLucky(1230)
