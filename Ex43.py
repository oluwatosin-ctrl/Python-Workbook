print("Historical Figure on Notes")

amount = int(input("Enter the amount to check who is on the note"))

if (amount == 100):
    person = "Benjamin Franklin"
elif (amount == 50):
    person ="Ulysses S.Grant"
elif (amount == 20):
    person = "Andrew Jackson"
elif (amount == 10):
    person = "Alexander Hamilton"
elif(amount == 5):
    person = "Abraham Lincoln"
elif(amount == 2):
    person = "Thomas Jefferson"
elif(amount == 1):
    person = "George Washington"
else:
    print("This amount does not exist as a $ note")

print("The person on the %d note is %s"%(amount,person))