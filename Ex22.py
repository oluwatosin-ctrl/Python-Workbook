from math import sqrt
s1 = int(input("Enter the length of one side"))
s2 = int(input("Enter the length of the second side"))
s3 = int(input("Enter the length of the third side"))

s = (s1+s2+s3)/2

area = sqrt(s*(s-s1)*(s-s2)*(s-s3))

print("The area of the triangle is ",area)