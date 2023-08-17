#Given the string, check if it is a palindrome.

def solution(inputString):
    return inputString[::-1] == inputString


print(solution("aaabaaaa"))
print(solution("z"))
print(solution("abacaba"))
print(solution("az"))
print(solution("a"))
print(solution("hlbeeykoqqqqokyeeblh"))
print(solution("abac"))
print(solution("aabaa"))
print(solution("zzzazzazz"))