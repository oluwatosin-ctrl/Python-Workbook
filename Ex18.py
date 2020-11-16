from math import pi

radius = int(input("Enter your radius"))
height = int(input("Enter your height"))

volume= pi*radius*radius*height

print(f"The volume of the cylinder is {volume:,.1f}")