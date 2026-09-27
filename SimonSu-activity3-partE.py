Travel_Distance = float(input("Enter distance (km): "))
Average_Speed = float(input("Enter average speed (km/h): "))
Fuel_Efficiency = float(input("Enter fuel efficiency of your car(km per liter): "))
Fuel_Price = float(input("Enter fuel price per liter: $"))
Number_Of_Passengers = float(input("Enter the number of passengers: "))

Travel_Time = Travel_Distance / Average_Speed
Fuel_Consumption = Travel_Distance / Fuel_Efficiency
Fuel_Cost = Fuel_Consumption * Fuel_Price
Cost_Per_Passenger = Fuel_Cost / Number_Of_Passengers

print("Estimated travel time: " + str(Travel_Time) + " hours")
print("Fuel consumption: " + str(Fuel_Consumption) + " liters")
print("Fuel cost: $" + str(Fuel_Cost))
print("Cost per passenger: $" + str(Cost_Per_Passenger))