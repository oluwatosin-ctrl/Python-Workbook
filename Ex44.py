print("Check Canadian Holidays(Consistent)")

day = int(input("Enter the day "))

month = input("Enter the month")

if day ==1 and month == "January":
    print("The holiday is New years")
elif day == 1 and month == "July":
    print("The holiday is Canada day")
elif day == 25 and month == "December":
    print("The holiday is Christmas day")
else:
    print("Omo idk oo")

