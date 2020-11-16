from math import cos,floor
IDEAL_GAS_CONSTANT = 8.314

PRESSURE = int(input("Enter the pressure "))
VOLUME = int(input("Enter the volume of the substance"))
TEMPERATURE = float(input("Enter the temperature (IN CELSIUS)"))



TEMPERATURE= TEMPERATURE+273

N_MOLES = (PRESSURE*VOLUME)/(IDEAL_GAS_CONSTANT*TEMPERATURE)

print(f"The no of moles of the substance is {N_MOLES:,.2f} ")
