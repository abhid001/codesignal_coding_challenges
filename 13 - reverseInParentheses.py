'''
Write a function that reverses characters in (possibly nested) parentheses in the input string.

Input strings will always be well-formed with matching ()s.

Example

For inputString = "(bar)", the output should be
solution(inputString) = "rab";
For inputString = "foo(bar)baz", the output should be
solution(inputString) = "foorabbaz";
For inputString = "foo(bar)baz(blim)", the output should be
solution(inputString) = "foorabbazmilb";
For inputString = "foo(bar(baz))blim", the output should be
solution(inputString) = "foobazrabblim".
Because "foo(bar(baz))blim" becomes "foo(barzab)blim" and then "foobazrabblim".
'''

import re
def reverseInParentheses(inputString):
    while "(" in inputString:
        match = re.search("\([^()]*\)", inputString)
        match_string = match.group(0)[1: len(match.group(0)) - 1]
        reversed_match_string = match_string[::-1]
        inputString = inputString[:match.start()] + reversed_match_string + inputString[match.end():]
    return inputString
  
 reverseInParentheses("(bar))
