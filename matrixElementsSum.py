def solution(matrix):
    total_sum  = 0
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    
    for col in range(num_cols):
        for row in range(num_rows):
            element = matrix[row][col]
            # print(f"Column {col}, Row {row}: {element}")
    
            if element == 0:
                break
            else:
                total_sum += element
    return total_sum

print(solution([[0,1,1,2], 
 [0,5,0,0], 
 [2,0,3,3]]))
print(solution([[1,1,1,0], 
 [0,5,0,1], 
 [2,1,3,10]]))
print(solution([[1,1,1], 
 [2,2,2], 
 [3,3,3]]))