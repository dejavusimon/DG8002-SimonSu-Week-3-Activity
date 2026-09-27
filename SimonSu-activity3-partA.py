cad = float(input("Enter the amount in CAD: $"))
usd = cad * 0.72
usd = int(usd * 100 + 0.5) / 100
print("Equivalent to $" + str(usd) + " USD")