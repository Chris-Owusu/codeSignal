def solution(inputString):
    stack = []
    result = []
    
    for char in inputString:
        if char == '(':
            stack.append(result)
            result = []
        elif char == ')':
            result = stack.pop() + list(reversed(result))
        else:
            result.append(char)
    
    return ''.join(result)


print(solution("(bar)")) 
print(solution("foo(bar)baz"))  
print(solution("foo(bar)baz(blim)"))
print(solution("foo(bar(baz))blim"))