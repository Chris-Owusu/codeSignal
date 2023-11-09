def solution(s1, s2):
    count = 0
    newSet = []
    for i in s1:
        for j in s2:
            if i == j and i not in newSet:
                count += 1
                newSet.append(i)
                newSet.append(j)
    return count, newSet


s1 = "aabcc"
s2 = "adcaa"

print(solution(s1, s2))


# def solution(s1, s2):
#     count = 0
#     char_count_s1 = {}
#     char_count_s2 = {}

#     # Count occurrences of each character in s1
#     for char in s1:
#         char_count_s1[char] = char_count_s1.get(char, 0) + 1

#     # Count occurrences of each character in s2
#     for char in s2:
#         char_count_s2[char] = char_count_s2.get(char, 0) + 1

#     # Find common characters and count their occurrences
#     for char, count_s1 in char_count_s1.items():
#         if char in char_count_s2:
#             count += min(count_s1, char_count_s2[char])

#     return count