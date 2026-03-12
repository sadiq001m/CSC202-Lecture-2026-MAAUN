class FuelPump:
    def __init__(self, pump_id, fuel_type, price_per_liter):
        self.pump_id = pump_id
        self.fuel_type = fuel_type
        self.price_per_liter = price_per_liter
        self.total_dispensed = 0

    def dispense(self, liters):
        self.total_dispensed += liters
        return liters * self.price_per_liter


# Instantiate a pump
pump1 = FuelPump("P1", "Petrol", 650)  # 650 per liter

# Dispense 20 liters
cost = pump1.dispense(20)

# Print the cost
print("Total cost:", cost)