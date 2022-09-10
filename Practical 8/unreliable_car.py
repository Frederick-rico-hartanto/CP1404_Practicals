from random import randint
from car import Car

class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        random_num = randint(0, 100)
        if random_num >= self.reliability:
            distance = 0
        driving_distance = super().drive(distance)
        return driving_distance