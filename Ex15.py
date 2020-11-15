FEET_TO_INCH = 12
FEET_TO_YARD = 0.3333
FEET_TO_MILES = 0.000189394

feet = int(input("Enter your number in feet"))

INCHES = feet*FEET_TO_INCH
YARDS = feet*FEET_TO_YARD
MILES = feet*FEET_TO_MILES

INCHES = float(INCHES)


print(f"The distance in inches is ", INCHES)
print(f"The distance in yards is {YARDS:,.2f}")
print(f"The distance in miles is ", MILES)