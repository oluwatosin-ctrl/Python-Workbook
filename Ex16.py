from math import pi

radius = float(input("Enter your radius value (in deccimal terms)"))

area = pi*(radius*radius)

volume = 0.75*(pi*(radius*radius*radius))

print(f"The area of the circle  is {area:,.2f}")

print(f"The volume of a sphere is {volume:,.2f}")

