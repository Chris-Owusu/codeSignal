# def solve(meal_cost, tip_percent, tax_percent):
#     tip_amount = (meal_cost / 100) * tip_percent
#     tax_amount = (meal_cost / 100) * tax_percent
#     total_cost = meal_cost + tip_amount + tax_amount
#     return round(total_cost)

# meal_cost = 12.00
# tip_percent = 20
# tax_percent = 8

# print(solve(meal_cost, tip_percent, tax_percent))

def solution(array):
    result = []
    flattened_array = [element for sublist in array for element in sublist]
    for elem in flattened_array:
        if elem not in result:
            result.append(elem)
    return result

print(solution([[3,5], [1,4], [2,4], [1,5]]))

