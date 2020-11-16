from math import tan

n = float(input("Enter number of sides of the polygon"))
s = float(input("Enter length of sides of the polygon "))

area = (n*s*s)/(4*tan(180/n))

print("The area of the",n," sided polygon is",area)