def solution(s):
    vowels = "aAeEiIoOuU"
    
    reverse_list = [i for i in s if i in vowels]
    reverse_list.reverse()
    
    vowel_index = 0
    final_list = []
    
    for elem in s:
        if elem in vowels:
            final_list.append(reverse_list[vowel_index])
            vowel_index += 1
        else:
            final_list.append(elem)
    
    return ''.join(final_list)

print(solution("Hello World"))
print(solution("Code Signal"))
print(solution("White Man"))
print(solution("Algorithm avengers"))