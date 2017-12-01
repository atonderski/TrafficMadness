from traffic_madness.car import Car
from traffic_madness.config import Config
from traffic_madness.car.lane_switching_car import LaneSwitchingCar

class AggressiveCar(LaneSwitchingCar):
    def __init__(self, position, velocity, lane):
        config = Config()
        super().__init__(position, velocity, lane)
        self.acceleration *= config.aggressiveness
        self.deceleration *= config.aggressiveness
        self.safetymultiplier /= config.aggressiveness

    def update(self, target_speed, nearby_cars):
        config = Config()
        distances = []  # Stores distances of neighbours
        # Cannot set to 0, else cars never brake
        target_speed *= config.aggressiveness

        super().update(target_speed, nearby_cars)
