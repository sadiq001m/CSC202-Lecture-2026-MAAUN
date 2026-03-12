from models import FuelDispenser, CarWash


# Create station assets
pump1 = FuelDispenser("Pump 1", 650, 120)   # price per liter, liters sold
pump2 = FuelDispenser("Pump 2", 650, 80)

wash1 = CarWash("Car Wash", 3000, 15)       # price per wash, cars washed


# Store all assets in one list
assets = [pump1, pump2, wash1]


# Calculate total revenue
total_revenue = 0

for asset in assets:
    revenue = asset.calculate_revenue()
    print(asset.name, "Revenue:", revenue)
    total_revenue += revenue


print("\nTotal Station Revenue:", total_revenue)