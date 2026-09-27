Principal_Amount = float(input("Enter principal amount: $"))
Interest_Rate = float(input("Enter interest rate (%): "))
Investment_Period = float(input("Enter time period (years): "))
Interest_Amount = Principal_Amount * Interest_Rate / 100 * Investment_Period
print("Interest accumulated: $" + str(Interest_Amount))