print("Check the type of Triangle with the size")

side1 = float(input("Enter the first size of the triangle"))
side2 = float(input("Enter the second side of the triangle"))
side3 = float(input("Enter the third side of the triangle"))

if (side1 == side2)or(side2 == side3) or (side1 == side3):
    name = "isoceles"
elif(side1 == side2)and(side2 == side3):
    name = "equilateral"
else:
    name = "scalene"

print("This is a",name,"triangle")
