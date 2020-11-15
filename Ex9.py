principal = float(input("Enter principal amount"))

INTEREST_RATE = 0.04

amount1 = (INTEREST_RATE*principal) + principal
amount2 = (INTEREST_RATE*amount1) + amount1
amount3 = (INTEREST_RATE*amount2) + amount2

print("The total amount after the first year is ",amount1)
print("The total amount after the second year is ",amount2)
print("The total amount after the third year is ",amount3)