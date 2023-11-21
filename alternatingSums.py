

def solution(a):
    sum_even = sum(a[i] for i in range(0, len(a), 2))
    sum_odd = sum(a[i] for i in range(1, len(a), 2))

    return [sum_even, sum_odd]

print(solution([50, 60, 60, 45, 70]))
