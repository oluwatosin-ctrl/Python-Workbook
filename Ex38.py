print("PROGRAM TO THE NUMBER OF DAYS A MONTH HAS")

month = str(input("Enter the month "))
if(month == 'January')| (month == 'March')|(month == 'May')|(month == 'July')|(month == 'October')|(month == 'December')|(month == 'August'):
    print("This month has 31 days")
elif(month == 'September')|(month == 'April')|(month =='June')|(month == 'November'):
    print("This month has 30 days")
else:
    print("THe month is february")