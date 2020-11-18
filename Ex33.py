
BREAD_PRICE = 3.49
NORMS_BREAD = int(input("Enter number of freshly baked bread you want to buy"))
OLD_BREAD = int(input("Enter the number of day old bread you are buying"))

PRICE_OLD = 0.6*OLD_BREAD
PRICE_NEW = BREAD_PRICE*NORMS_BREAD

TOTAL = PRICE_OLD+PRICE_NEW

print(f"The total amount is {TOTAL:,.2F}")