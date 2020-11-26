print("Program to determine the next day")

year = int(input("Enter the year "))
month = int(input("Enter the month"))
date = int(input("Enter the day"))

if(month > 12 or date > 31):
    print("This is not a valid ")
elif(month == 12 and date == 31):
    date = 1
    month = 1
    year += 1
    print("Tomorrow's date would be ", date , "-", month,"-", year,".")
elif((date == 29 or date == 28) and month == 2):
    date = 1
    month += 1
    print("Tomorrow's date would be ", date, "-", month,"-",year, ".")
elif((month == 9 or month == 4 or month == 5 or month == 11 ) and date == 30):
    date = 1
    month += 1
    print("Tomorrow's date would be ", date, "-", month, "-", year, ".")
elif((month == 1 or month == 3 or month == 6 or month == 7 or month == 8 or month == 10 or month == 12) and date == 31):
    date = 1
    month += 1
    print("Tomorrow's date would be ", date, "-", month, "-", year, ".")
else:
    print("this")