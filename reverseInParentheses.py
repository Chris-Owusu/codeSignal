def solution(inputString):
    translation_table = str.maketrans("", "", "()")
    inputString.translate(translation_table)
    return inputString[::-1]

inputString = "(bar)"
print(solution(inputString))