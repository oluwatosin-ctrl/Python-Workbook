magnitude = float(input("Enter the magnitude of the earthquake "))

if (magnitude < 2.0):
    print("The magnitude of the earthquake is Micro")
elif(magnitude>=2.0 and magnitude<=3.0):
    print("The magnitude of the earthquake is Very Minor")
elif(magnitude>=3.0 and magnitude<=4.0):
    print("The magnitude of the earthquake is  Minor")
elif(magnitude>=4.0 and magnitude<=5.0):
    print("The magnitude of the earthquake is Light")
elif(magnitude>=5.0 and magnitude<=6.0):
    print("The magnitude of the earthquake is Moderate")
elif(magnitude>=6.0 and magnitude<=7.0):
    print("The magnitude of the earthquake is Strong")
elif(magnitude>=7.0 and magnitude<=8.0):
    print("The magnitude of the earthquake is Major")
elif(magnitude>=8.0 and magnitude<=10.0):
    print("The magnitude of the earthquake is Great")
elif(magnitude<10.0):
    print("The magnitude of the earthquake is Meteoric")
else:
    print("Omo idk")