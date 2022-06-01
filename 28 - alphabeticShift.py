'''
Given a string, your task is to replace each of its characters by the next one in the English alphabet; i.e. replace a with b, replace b with c, etc (z would be replaced by a).

Example

For inputString = "crazy", the output should be solution(inputString) = "dsbaz".
'''

def solution1(inputString):
    op_str = ''
    for ch in inputString:
        if ch == 'z':
            op_str += 'a'
        else:
            op_str += chr(ord(ch)+1)
    return op_str

# better solution
def solution2(inputString):

    return ''.join([chr(ord(ch)+1) if ch != 'z' else 'a' for ch in inputString])
