no_of_persons = int(input("Enter the number of attendants "))
number = 0
cost = 0

while(number != no_of_persons):
    age = int(input("Enter the age of the individual"))
    number +=1
    if(age >= 3 & age<=12):
        cost += 14
    elif(age> 12 & age < 65):
        cost += 23
    elif(age >=65):
        cost += 18

   

print(f"The total is {cost:,.2f}")


