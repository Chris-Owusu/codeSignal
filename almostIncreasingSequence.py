def solution(sequence):
    count = 0
    if len(sequence) == 1:
        return True
    for el in range(1, len(sequence)):
        if sequence[el] <= sequence[el - 1]:
            count += 1
            if count > 1:
                return False
        if el > 1 and sequence[el] <= sequence[el - 2]:
                sequence[el] = sequence[el - 1]
    return True

print(solution([1, 3, 2, 1]))
print(solution([1, 3, 2]))
print(solution([1, 2, 1, 2]))
print(solution([3, 6, 5, 8, 10, 20, 15]))
print(solution([1, 1, 2, 3, 4, 4]))
print(solution([1, 4, 10, 4, 2]))
print(solution([10, 1, 2, 3, 4, 5]))