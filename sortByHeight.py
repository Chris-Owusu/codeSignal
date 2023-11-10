def solution(a):
    ind = sorted(i for i in a if i != -1)
    newList = []
    idx = 0

    for el in a:
        if el == -1:
            newList.append(el)
        else:
            newList.append(ind[idx])
            idx += 1
        
    return newList




a = [-1, 150, 190, 170, -1, -1, 160, 180]
print(solution(a))
print(solution([-1, -1, -1, -1, -1]))
print(solution([-1]))
print(solution([4, 2, 9, 11, 2, 16]))
print(solution([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1]))
print(solution([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3]))