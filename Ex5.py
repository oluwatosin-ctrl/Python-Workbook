#NO OF CONTAINERS REFUND

#AMOUNT GOTTEN FROM EACH BOTTLE
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

less = int(input("Enter the number of 1 litre(or less) bottles you have"))
more = int (input("Enter number of bottles greater than 1 litres you have"))



total = (less*LESS_DEPOSIT)+(more*MORE_DEPOSIT)

print(f"The total no amount pgotten from the refund is ${total:,.2f}")