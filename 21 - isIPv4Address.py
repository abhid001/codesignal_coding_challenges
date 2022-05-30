'''
An IP address is a numerical label assigned to each device (e.g., computer, printer) participating in a computer network that uses the Internet Protocol for communication. There are two versions of the Internet protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
solution(inputString) = true;

For inputString = "172.316.254.1", the output should be
solution(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
solution(inputString) = false.

There is no first number.
'''
def solution(inputString):
    a = inputString.split(".")
    def isIPv4(s):
        try: 
            return str(int(s)) == s and 0 <= int(s) < 256
        except: 
            return False

    if inputString.count(".") == 3 and all(isIPv4(i) for i in a):
        return True

    return False
