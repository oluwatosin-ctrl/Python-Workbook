days = int(input("Enter the time in days"))
hours= int(input("Enter the time in hours"))
minutes=int(input("Enter the tinme in minutes"))
seconds = int(input("Enter the time in seconds"))

days = days * 86400
hours = hours * 3600
minutes = minutes * 60
seconds = seconds

totalseconds = days+hours+minutes+seconds

print(totalseconds)
