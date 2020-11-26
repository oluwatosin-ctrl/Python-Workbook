print("Program to determine if a year is a leap year or not")

YEAR_ENTERED = int(input("Enter the year to determine if its a leap year or not"))

if (YEAR_ENTERED % 400 == 0):
    isLeapyear = True
elif(YEAR_ENTERED % 100 == 0):
    isLeapyear = False
elif(YEAR_ENTERED % 4 == 0):
    isLeapyear = True

    if isLeapyear:
        print(YEAR_ENTERED," is a leap year")
else:
    print(YEAR_ENTERED," is not a leap year")