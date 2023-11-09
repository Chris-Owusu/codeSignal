def solution(n):
    n_str = str(n)
    mid = len(n_str) // 2
    left = list(map(int, n_str[:mid]))
    right = list(map(int, n_str[mid:]))

    return sum(left) == sum(right)




print(solution(1234))
print(solution(239017))
print(solution(10))