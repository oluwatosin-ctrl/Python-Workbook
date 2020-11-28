grade = input("Enter your grade(Enter a blank line to quit)")
counter = 0
point = 0


while(grade != ""):
    grade = input("Enter your grade(Enter a blank line to quit)")
    
    counter += 1
    if (grade == "A+"):
        point += 5.0
    elif(grade == "A"):
        point += 4.0
    elif(grade == "A-"):
        point += 3.7
    elif(grade == "B+"):
        point += 3.3
    elif(grade == "B"):
        point += 3.0
    elif(grade == "B-"):
        point +=  2.7
    elif(grade == "C+"):
        point += 2.3
    elif(grade == "C"):
        point += 2.0
    elif(grade == "C-"):
        point += 1.7
    elif(grade == "D+"):
        point += 1.3
    elif(grade == "D"):
        point += 1.0 
    elif(grade == "F"):
        point += 0.0
    else:
        print("An Error Ocurred")
    
   
    
GPA = point/ counter

print(f"Ended {GPA:,.2f}")
