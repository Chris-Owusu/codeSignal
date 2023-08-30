def solution(strings, sources):
    result = []
    for src in sources:
        found = False
        for i in range(len(strings) - 1):
            if src == strings[i] + strings[i+1]:
                found = True
                break
        result.append(found)
    return result

strings = ["one", "two", "three"]
sources = ["onetwo", "random", "one", "twoone", "twothree"]
print(solution(strings, sources))  # Output: [True, False, True, False, False]