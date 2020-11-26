from string import  ascii_lowercase , ascii_uppercase

plate = input("Enter the License plate number")

if len(plate) == 6 and plate[0]>= "A" and plate[0]<="Z" and \
    plate[1] >= "A" and plate[1] <= "Z" and \
    plate[2] >= "A" and plate[2] <= "Z" and \
    plate[3] >= "O" and plate[3] <= "9" and \
    plate[4] >= "O" and plate[4] <= "9" and \
    plate[5] >= "O" and plate[5] <= "9":
    print("The plate is an older styled plate")
elif len(plate) == 7 and plate[0]>= "0" and plate[0]<="9" and \
    plate[1] >= "O" and plate[1] <= "9" and \
    plate[2] >= "O" and plate[2] <= "9" and \
    plate[3] >= "O" and plate[3] <= "9" and \
    plate[4] >= "A" and plate[4] <= "Z" and \
    plate[5] >= "A" and plate[5] <= "Z" and \
    plate[6] >= "A" and plate[6] <= "Z":
    print("The plate is the newer styled plate")
else:
    print("This plate number is not valid")