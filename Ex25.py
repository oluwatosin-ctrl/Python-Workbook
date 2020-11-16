seconds = int(input("Enter the total time in seconds "))

days = seconds/ 86400
days = days %86400

hours = seconds/3600
hours = hours % 3600

minutes = seconds/60
minutes = minutes % 60

seconds = seconds % 60

print(f"Days:{days:,.0f} Hours:{hours:,.0f} Minutes:{minutes:,.0f} Seconds:{seconds:,.0f}")

