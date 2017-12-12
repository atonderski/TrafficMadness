from traffic_madness.car.lane_switching_car import LaneSwitchingCar
from traffic_madness.config import Config


class PassiveCar(LaneSwitchingCar):
    def __init__(self, position, velocity, lane, nice):
        config = Config()
        super().__init__(position, velocity, lane, nice)
#        self.acceleration *= config.passiveness
#        self.deceleration *= config.passiveness
        self.safetymultiplier /= config.passiveness
        self.color = (0, 255, 0)

    def update(self, target_speed, nearby_cars):
        config = Config()
        target_speed *= config.passiveness

        super().update(target_speed, nearby_cars)
