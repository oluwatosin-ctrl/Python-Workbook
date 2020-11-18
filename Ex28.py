print("Program to calculate wind chill index")

airtemp = float(input("Enter the given Air Temperature"))
windspeed = float(input("Enter the present wind speed"))

WCI = 13.12 + (0.6215*airtemp) - (11.37*windspeed) + (0.3965*airtemp*windspeed)

print(f"The value of the wind chill index is {WCI:,.2f}")
