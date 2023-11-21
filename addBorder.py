# Given a rectangular matrix of characters, add a border of asterisks(*) to it.

def solution(picture):
    pic_len = len(picture)
    elem_len = len(picture[0])
    
    border = ["*" * (elem_len + 2)]
    
    for input in picture:
        border.append("*" + input + "*")

    border.append("*" * (elem_len + 2))
    
    return border

print(solution(["abc",
           "ded"]))
