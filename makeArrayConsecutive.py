def solution(statues):
    statues.sort()
    count = 0
    for i in range(len(statues) - 1):
        if statues[i] + 1 != statues[i + 1]:
            count += statues[i + 1] - statues[i] - 1
    return count
    
print(solution([6, 2, 3, 8]))
print(solution([0, 3]))
print(solution([5, 4, 6]))
print(solution([6, 3]))