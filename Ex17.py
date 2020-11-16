TIMING = 8.9
KILO_WATT = 2.77778e-7
SHC_WATER = 4.186

mass = int(input("Enter the mass of water"))

temperature= int(input("Enter the temperature difference"))

quan_heat = SHC_WATER*mass*temperature

print(f"The quantity of heat is {quan_heat:,.2f}")

COST = quan_heat*KILO_WATT*TIMING

print(f"The cost will be ",COST)

