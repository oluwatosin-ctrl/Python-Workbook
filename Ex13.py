CENTS_PER_TOONIE = 200
CENTS_PER_LOONIE = 100
CENTS_PER_QUARTER = 25
CENTS_PER_DIME = 10
CENTS_PER_NICKEL = 5

cents = int(input("Enter amount in cents"))

print("", cents//CENTS_PER_TOONIE,"toonies")
cents = cents % CENTS_PER_TOONIE

print("", cents // CENTS_PER_LOONIE, "loonies")
cents = cents % CENTS_PER_LOONIE

print("",cents//CENTS_PER_QUARTER,"quarters")
cents = cents % CENTS_PER_QUARTER

print("", cents // CENTS_PER_DIME,"dimes")
cents = cents % CENTS_PER_DIME

print("",cents//CENTS_PER_NICKEL,"nickels")
cents = cents % CENTS_PER_NICKEL


