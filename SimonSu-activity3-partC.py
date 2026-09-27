Bill = float(input("Enter bill amount: $"))
Tip_Percent = float(input("Enter tip percentage (%): "))
Number_Of_People = float(input("Enter number of people "))
Tip_Amount = Bill * Tip_Percent / 100
Total_Amount = Bill + Tip_Amount
Amount_Per_Person = Total_Amount / Number_Of_People
print("Tip: $" + str(Tip_Amount))
print("Total: $" + str(Total_Amount))
print("Each person owes: $" + str(Amount_Per_Person))