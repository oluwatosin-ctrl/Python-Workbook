print("Program to check season of the year")

month = input("Enter the month")
day = int(input("Enter the day of the month"))
if day > 31:
    print("There is an Error")
else:
    if (month == "May" or month == "April") or (month == "March" and day >= 20) or (day <= 21 and month == "June"):
        print("This season is Spring")
    elif (month == "July" or month == "August") or (month == "June" and day > 21) or (day <= 22 and month == "September"):
        print("This is Summer")
    elif (month == "October" or month == "November") or (month == "September" and day > 22) or (month == "December" and day <=21):
        print("The season is Fall")
    elif(month == "January" or month == "February") or (month == "December" and day>21) or (month == "March" and day<20):
        print("Winter is here")