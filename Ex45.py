print("Program to check if a box on a board is black or white")

position = input("Enter the position you want to check(in this order \"C4\")")

letter = position[0]
num = position[1]
num = int(num)

if (letter == "A" and (num % 2 == 0)) or (letter == "B" and (num % 2 == 1)) or (letter == "C" and (num % 2 == 0)) or (letter == "D" and (num % 2 == 1)):
    print("This space is white")

elif(letter == "E" and (num % 2 ==0)) or (letter == "F" and (num % 2 == 1)) or (letter == "G" and (num % 2 == 0)) or (letter == "H" and (num % 2 == 1)):
    print("This space is white")
else:
    print("This space is black")