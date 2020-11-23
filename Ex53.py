print("Program to detrmine meanings of your employee ratings")

rating = float(input("Enter your employee rating"))



increase = 2400*rating

if (rating == 0.0):
    print(f"Your performance this past year has been Unacceptable, Your stipulated raise this year is ${increase:,.2f}")
elif(rating == 0.4):
    print(f"Your performance this past year has been Acceptable, Your stipulated raise this year is {increase:,.2f}")
elif(rating == 0.6):
    print(f"Your performance this past year has been Meritorious, Your stipulated raise this year is {increase:,.2f}")
else:
    print("Please pack your bags and leave the premises")
