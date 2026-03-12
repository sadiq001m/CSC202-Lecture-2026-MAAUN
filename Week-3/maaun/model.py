from abc import ABC, abstractmethod


# Abstract Base Class
class StationAsset(ABC):

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_revenue(self):
        pass


# Fuel Dispenser Class
class FuelDispenser(StationAsset):

    def __init__(self, name, price_per_liter, liters_sold):
        super().__init__(name)
        self.price_per_liter = price_per_liter
        self.liters_sold = liters_sold

    def calculate_revenue(self):
        return self.price_per_liter * self.liters_sold


# Car Wash Class
class CarWash(StationAsset):

    def __init__(self, name, price_per_wash, cars_washed):
        super().__init__(name)
        self.price_per_wash = price_per_wash
        self.cars_washed = cars_washed

    def calculate_revenue(self):
        return self.price_per_wash * self.cars_washed

