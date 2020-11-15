from math import sin,cos,acos,radians

print("WELCOME TO PROGRAM TO CALCULATE DISTANCE ON THE EARTH SURFACE")

t1 = float(input("Enter latitude coordinates t1 where (t1,g1)"))

g1 = float(input("Enter latitude coordinates g1 "))

t2 = float(input("Enter longitude coordinates t2 where (t2,g2)"))

g2 = float(input("Enter longitude coordinates g2"))

distance = 6371.01 * acos(sin(t1)*sin(t2)*cos(t1)*cos(t2)*cos(g1 - g2))

distance = radians(distance)

print(f"The distance between these coordinates (",t1, ",",g1,") and (",t2,",",g2,")is distance:,.%2f} km ")