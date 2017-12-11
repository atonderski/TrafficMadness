from traffic_madness.config import Config
from traffic_madness.car.lane_switching_car import LaneSwitchingCar


class AggressiveCar(LaneSwitchingCar):
    def __init__(self, position, velocity, lane, nice):
        config = Config()
        super().__init__(position, velocity, lane, nice)
        self.acceleration *= config.aggressiveness
        self.deceleration *= config.aggressiveness
        self.safetymultiplier /= config.aggressiveness
        self.color = (255, 0, 0)
        self.delay_buffer = []

    def update(self, target_speed, nearby_cars):
        config = Config()
        target_speed *= config.aggressiveness

        super().update(target_speed, nearby_cars)
