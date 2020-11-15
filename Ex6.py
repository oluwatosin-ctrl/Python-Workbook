MEAL_COST = float(input("Enter how much the meal costs :"))

tax = 0.075*MEAL_COST;
tip =  0.18 * MEAL_COST;

print(f"The tip for this meal is {tip:,.2f}")

print(f"The tax payable for this meal is {tax:,.2f}")

TOTAL_MEAL_COST = tax + tip + MEAL_COST
print(f"The total amount is {TOTAL_MEAL_COST:,.2f}")