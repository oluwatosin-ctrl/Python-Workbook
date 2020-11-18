kilopascals = float(input("Enter the pressure in kilopascals "))

pounds = kilopascals/6.895

millimercury = kilopascals*7.501

atmosphere= kilopascals/101

print(f"The pressure of {kilopascals:,.2f} in kilopascals is {pounds:,.2f} pounds per square inch")
print(f"The pressure of {kilopascals:,.2f} in kilopascals is {millimercury:,.2f} millimeter per mercury")
print(f"The pressure of {kilopascals:,.2f} in kilopascals is {atmosphere:,.2f} atmospheres")