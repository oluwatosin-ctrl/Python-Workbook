print("CONVERSION OF HUMAN YEARS TO DOG YEARS")
HUMAN_YEARS = int(input("Enter the human years"))
DOG_YEARS = 0

if(HUMAN_YEARS >= 2 ):
    if(HUMAN_YEARS ==2):
        HUMAN_YEARS = 0
    DOG_YEARS = 10.5
    DOG_YEARS = ((HUMAN_YEARS-2)*4)+10.5
    print("The dog is",DOG_YEARS,"years old ")





else:
    print("There is an error ")

