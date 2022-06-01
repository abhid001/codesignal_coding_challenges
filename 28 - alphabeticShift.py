'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
'''

def solution(inputString):
    op_str = ''
    for ch in inputString:
        if ch == 'z':
            op_str += 'a'
        else:
            op_str += chr(ord(ch)+1)
    return op_str
