def solution(a, b):
    # Find the indices where the elements differ
    diff_indices = [i for i in range(len(a)) if a[i] != b[i]]

    # Return True if there are no differences or exactly two differences
    return len(diff_indices) == 0 or (len(diff_indices) == 2 and a[diff_indices[0]] == b[diff_indices[1]] and a[diff_indices[1]] == b[diff_indices[0]])
#     if len(a) != len(b):
#         pass
#     else:
#         for i in range(len(a)):
#             for j in range(len(b)):
#                 if j == i:
#                     return True
#                 else:
#                     return False

print(solution([1, 2, 3], [1, 2, 3])) # True
print(solution([1, 2, 3], [2, 1, 3])) # True
print(solution([1, 2, 2], [2, 1, 1])) # False
print(solution([1, 2, 1, 2], [2, 2, 1, 1])) # True
print(solution([1, 2, 1, 2, 2, 1], [2, 2, 1, 1, 2, 1])) # True
print(solution([1, 1, 4], [1, 2, 3])) # False

