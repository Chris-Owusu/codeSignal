def solution(s1, s2):
    count = 0
    newSet = set()
    for i in s1:
        for j in s2:
            if j == i and j not in newSet:
                count += 1
                newSet.add(j)
    return count



s1 = "aabcc"
s2 = "adcaa"

print(solution(s1, s2))