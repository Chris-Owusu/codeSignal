#Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

def solution(year):
    if 1 <= year <= 100:
        return 1
    elif 101 <= year <= 200:
        return 2
    else:
        return (year - 1) // 100 + 1


print(solution(1905))
print(solution(1700))
print(solution(1988))
print(solution(2000))
print(solution(2001))
print(solution(200))
print(solution(374))
print(solution(45))
print(solution(4))
print(solution(1222))