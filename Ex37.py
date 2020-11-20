print("PROGRAM TO CHECK NAME OF SHAPE BASED ON NUMBER OF SIDES")

number_of_sides = int(input("Enter the number of sides of the given shape"))

if(number_of_sides == 3):
    print("The shape is a triangle")
elif(number_of_sides == 4):
    print("The shape is either a rectangle or square")
elif(number_of_sides == 5):
    print("The shape is a pentagon")
elif(number_of_sides == 6):
    print("The shape is a hexagon")
elif(number_of_sides == 7):
    print("The shape is a heptagon")
elif(number_of_sides == 8):
    print("The shape is an octagon")
elif(number_of_sides == 9):
    print("The shape is a nonagon")
elif(number_of_sides == 10):
    print("This is a decagon")
else:
    print("Omo na your own be that")