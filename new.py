def solve(meal_cost, tip_percent, tax_percent):
    tip_amount = (meal_cost / 100) * tip_percent
    tax_amount = (meal_cost / 100) * tax_percent
    total_cost = meal_cost + tip_amount + tax_amount
    return round(total_cost)

meal_cost = 12.00
tip_percent = 20
tax_percent = 8

print(solve(meal_cost, tip_percent, tax_percent))