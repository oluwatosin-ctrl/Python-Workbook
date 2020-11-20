from math import sqrt

print("From the quardatic equation")
a = int(input("Enter the value of a in the equation"))
b = int(input("Enter the value of b in the equation"))
c = int(input("Enter the value of c in the equation"))

sol1 = -b + sqrt((b*b)- 4*a*c)

x1 = sol1/2*a

sol2 = -b - sqrt((b*b)- 4*a*c)

x2 = sol2/2*a

print("The roots of the quadratic equation are", x1," ,",x2)
