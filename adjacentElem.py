#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
def solution(inputArray):
    max = inputArray[0] * inputArray[1]
    
    for i in range(1, len(inputArray) - 1):
        adj = inputArray[i] * inputArray[i+1]
        if adj > max:
            max = adj
    return max
    

print(solution([3, 6, -2, -5, 7, 3]))
print(solution([-1, -2]))
print(solution([5, 1, 2, 3, 1, 4]))
print(solution([1, 2, 3, 0]))
print(solution([9, 5, 10, 2, 24, -1, -48]))
print(solution([5, 6, -4, 2, 3, 2, -23]))