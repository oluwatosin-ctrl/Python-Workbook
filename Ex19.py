from math import sqrt
acceleration = 9.8

initial =int(input("Enter initial velocity"))
distance = int(input("Enter distance covered"))

final = (initial*initial) + 2*acceleration*distance
final = float(sqrt(final))

print(f"The final speed of the object is {final:,.2f} ")
