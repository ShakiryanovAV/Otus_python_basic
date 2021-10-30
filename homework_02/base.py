from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    weight = 3000
    started = False
    fuel = 50
    fuel_consumption = 1  # liters per km

    def __init__(self, weight, fuel, fuel_consumption):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.started is False:
            if self.fuel <= 0:
                raise LowFuelError
            else:
                self.started = True

    def move(self, distance):
        required_fuel = distance * self.fuel_consumption
        if self.fuel >= required_fuel:
            self.fuel = self.fuel - required_fuel
        else:
            raise NotEnoughFuel
