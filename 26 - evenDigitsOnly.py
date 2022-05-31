'''
Check if all digits of the given integer are even.

Example

For n = 248622, the output should be
solution(n) = true;
For n = 642386, the output should be
solution(n) = false.

'''
def solution(n):
    return all((True if digit in ('0', '2', '4', '6', '8') else False for digit in str(n)))
