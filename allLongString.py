def solution(inputArray):
    result = []
    for el in inputArray:
        maxLen = max(inputArray, key=len)
        if len(el) == len(maxLen):
            result.append(el)
    return result



inputArray = ["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"]

print(solution(inputArray))